#!/usr/bin/python
# -*- coding: utf-8 -*-

# send mails to users who have only questions on forum (no forms or smth else)

import sys
sys.path += ['/var/www/lk']

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'lk.settings'

import django
django.setup()

from lkforms.models import UserProfile, External
from django.utils import timezone
from django.core import mail

def send_mails_forumonly():
    y, m = timezone.now().year, timezone.now().month
    if m > 6:
        deadline = timezone.now().replace(month = m - 6)
    else:
        deadline = timezone.now().replace(year = y - 1, month = m + 6)
    log_txt = ['send mails to users with only forum-activity for half-year since registration (before {0:%d}-{0:%m}-{0:%Y} {0:%H}:{0:%M})'.format(deadline
                                                                                                                                                ), '']
    log_file = ['{0:%d}-{0:%m}-{0:%Y} {0:%H}:{0:%M} mails sent (delete in 3 days)\n'.format(timezone.now())]
    ext = External.objects.get(id=80)  # letter
    for u in UserProfile.objects.order_by('created'):
        if u.user.date_joined > deadline:
            break
        elif not u.user.qnans_profile.count():
            pass
        elif u.answer_profile.count():
            pass
        elif u.regres_profile.count():
            pass
        elif (u.archregres_profile.count() + u.archanswer_profile.count() + u.user.own_forms.count() + u.user.edit_forms.count() +
               u.user.read_forms.count() + u.user.use_forms.count() + u.user.own_external.count() + u.user.receiver_profile.count() +
               u.user.own_mforms.count() + u.user.edit_mforms.count() + u.user.read_mforms.count() + u.user.own_mqns.count() +
               u.user.req_list.count() + u.user.mod_list.count() + u.user.qreq_list.count() + u.user.qmod_list.count() ) == 0:
            log_str = '<a href="http://lk.internat.msu.ru/admin/auth/user/{4}/delete/">{0} {1} {2}</a> {3:%d}-{3:%m}-{3:%Y} {3:%H}:{3:%M}'.format(
                u.sname.encode('utf8'), u.name.encode('utf8'), u.pname.encode('utf8'), u.created, u.user.id)
            connection = mail.get_connection()
            msg = mail.EmailMessage(ext.letter_abs, ext.letter + '\n--\n\nThis letter is generated automatically. Responses are not processed.',
                                    'Личный Кабинет СУНЦ МГУ <auto@automail.aesc.msu.ru>', [u.user.email, ])
            try:
                connection.send_messages([msg, ])
            except Exception:
                log_txt.append(' - '.join([log_str, "error, cannot send email"]))
            else:
                log_txt.append(' - '.join([log_str, "email sent"]))
            log_file.append('{}\n'.format(u.id))
    log_file.append('the end')
    log_txt.extend(['', 'the end'])
    f = open('/var/www/lk/logs/forumonly.log', 'wb')
    f.writelines(log_file)
    return log_txt

def check_file_forumonly():
    f = open('/var/www/lk/logs/forumonly.log', 'r')
    data = f.readlines()
    log_txt = [data[0], '']
    for i in range(1, len(data)-1):
        u = UserProfile.objects.get(id = data[i].split()[0])
        log_str = '<a href="http://lk.internat.msu.ru/admin/auth/user/{4}/delete/">{0} {1} {2}</a> {3:%d}-{3:%m}-{3:%Y} {3:%H}:{3:%M}'.format(
            u.sname.encode('utf8'), u.name.encode('utf8'), u.pname.encode('utf8'), u.created, u.user.id)
        if (u.answer_profile.count() + u.regres_profile.count() + u.archregres_profile.count() + u.archanswer_profile.count() +
                u.user.own_forms.count() + u.user.edit_forms.count() + u.user.read_forms.count() + u.user.use_forms.count() +
                u.user.own_external.count() + u.user.receiver_profile.count() + u.user.own_mforms.count() + u.user.edit_mforms.count() +
                u.user.read_mforms.count() + u.user.own_mqns.count() + u.user.req_list.count() + u.user.mod_list.count() +
                u.user.qreq_list.count() + u.user.qmod_list.count()) == 0:
            log_txt.append(' - '.join([log_str, "still nothing"]))
        else:
            log_txt.append(' - '.join([log_str, "smth new"]))
    log_txt.extend(['','the end'])
    return log_txt

def delete_forumonly():
    f = open('/var/www/lk/logs/forumonly.log', 'r')
    data = f.readlines()
    log_txt = [data[0], '']
    for i in range(1, len(data)-1):
        u = UserProfile.objects.get(id=data[i].split()[0])
        log_str = '{0} {1} {2} {3:%d}-{3:%m}-{3:%Y} {3:%H}:{3:%M}'.format(u.sname.encode('utf8'), u.name.encode('utf8'),
                                                                          u.pname.encode('utf8'), u.created)
        if (u.answer_profile.count() + u.regres_profile.count() + u.archregres_profile.count() + u.archanswer_profile.count() +
                u.user.own_forms.count() + u.user.edit_forms.count() + u.user.read_forms.count() + u.user.use_forms.count() +
                u.user.own_external.count() + u.user.receiver_profile.count() + u.user.own_mforms.count() + u.user.edit_mforms.count() +
                u.user.read_mforms.count() + u.user.own_mqns.count() + u.user.req_list.count() + u.user.mod_list.count() +
                u.user.qreq_list.count() + u.user.qmod_list.count()) == 0:
            u.user.delete()
            log_txt.append(' - '.join([log_str, "deleted"]))
        else:
            log_txt.append(' - '.join([log_str, "<a href='http://lk.internat.msu.ru/admin/auth/user/{}/delete/'>smth new</a>".format(u.user.id)]))
    log_txt.extend(['', 'the end'])
    f = open('/var/www/lk/logs/forumonly.log', 'w')
    f.writelines([data[0], 'the end'])
    return log_txt

if __name__ == "__main__":
    print 'it is just script'
    for d in send_mails_forumonly():
        print d
    print 'the end'
