#!/usr/bin/python
# -*- coding: utf-8 -*-

# delete users that have no actions (and no relations accept user-profile) and have registered more than half year ago

import sys
sys.path += ['/var/www/lk']

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'lk.settings'

import django
django.setup()
 
from lkforms.models import UserProfile, External
from django.utils import timezone
from django.core import mail

def delete_noaction():
    m, y = timezone.now().month, timezone.now().year
    if m > 6 :
        deadline = timezone.now().replace(month = m - 6)
    else:
        deadline = timezone.now().replace(month = m + 6, year = y -1)
    log_txt = ['delete users with absolutely no actions for half-year since registration (before {0:%Y}-{0:%m}-{0:%d} {0:%H}:{0:%M})'.format(deadline), '']
    ext = External.objects.get(id=105)    # letter
    deleted = 0
    for u in UserProfile.objects.order_by('created'):
        if u.user.date_joined > deadline:
            break
        elif u.answer_profile.count():
            pass
        elif u.regres_profile.count():
            pass
        elif u.user.qnans_profile.count():
            pass
        elif ( u.archregres_profile.count() + u.archanswer_profile.count() + u.user.own_forms.count() + u.user.edit_forms.count() + u.user.read_forms.count() + u.user.use_forms.count() + u.user.own_external.count() + u.user.receiver_profile.count() + u.user.own_mforms.count() + u.user.edit_mforms.count() + u.user.read_mforms.count() + u.user.own_mqns.count() + u.user.req_list.count() + u.user.mod_list.count() + u.user.qreq_list.count() + u.user.qmod_list.count() ) == 0:
            log_str = '{0} {1} {2} {3:%d}-{3:%m}-{3:%Y} {3:%H}:{3:%M}'.format(u.sname.encode('utf8'), u.name.encode('utf8'), u.pname.encode('utf8'), u.created)
            connection = mail.get_connection()
            msg = mail.EmailMessage(ext.letter_abs, ext.letter + '\n--\n\nThis letter is generated automatically. Responses are not processed.', 'Личный Кабинет СУНЦ МГУ <auto@automail.aesc.msu.ru>', [u.user.email,])
            try:
                connection.send_messages([msg,])
            except Exception:
                log_txt.append(' - '.join([log_str, "error, cannot send email"]))
            else:
                u.user.delete()
                deleted += 1
                log_txt.append(' - '.join([log_str, "email sent", "deleted"]))
    log_txt.extend(['', '{} users deleted'.format(deleted), 'the end'])
    return log_txt	         

if __name__ == "__main__":
    print 'it is just script'
    for d in delete_noaction():
        print d
    print 'the end'

       
