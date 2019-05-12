#!/usr/bin/python
# -*- coding: utf-8 -*-

# remind about something

import sys
sys.path += ['/var/www/lk']

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'lk.settings'

import django
django.setup()
 
from lkforms.models import Form, RegRes, External, UserProfile
from django.core import mail
#from lkfoms.views import user_identify
import csv
from django.core import mail

plus_checked = [ 229, ]
plus_passed = [ ]
minus_checked = [ ]
minus_passed = [ ]
check_permission = True
permission = '778'
letter = '12'

def make_remind_list():
    log_txt = ["list for reminding: \n"]

    for fm in [Form.objects.get(id=form) for form in plus_checked]:
        log_txt.append("+ checked " + fm.name + "\n")
    ulist = [r.user for r in RegRes.objects.filter(form__id__in = plus_checked)]
    log_txt.append(str(len(ulist)) + " users + \n")

    for fm in [Form.objects.get(id=form) for form in plus_passed]:
        log_txt.append("+ passed " + fm.name + " \n")
    ulist2 = [r.user for r in RegRes.objects.filter(form__id__in = plus_passed, short_result = '1')]
    log_txt.append(str(len(ulist2)) + " users + \n")

    ulist = list(set(ulist) | set(ulist2))

    for fm in [Form.objects.get(id=form) for form in minus_checked]:
        log_txt.append("- checked " + fm.name + "\n")
    done_list = [r.user for r in  RegRes.objects.filter(form__id__in = minus_checked)]
    log_txt.append(str(len(done_list)) + " users - \n")

    for fm in [Form.objects.get(id=form) for form in minus_passed]:
        log_txt.append("- passed " + fm.name + " \n")
    done2_list = [r.user for r in RegRes.objects.filter(form__id__in = minus_passed, short_result = '1')] 
    log_txt.append(str(len(done2_list)) + " users - \n")

    ulist = list(set(ulist) - set(done_list) - set(done2_list))
    log_txt.append("the rest " + str(len(ulist)) + "\n")

    if check_permission:
        no_remind = []
        for u in ulist:
            if 'no' in u.answer_profile.filter(question__id = permission)[0].answer:
                no_remind.append(u)
        ulist = list(set(ulist) - set(no_remind))
    log_txt.append("to remind " + str(len(ulist)) + "\n")

    remind = [ [u.sname.encode('utf8'), u.name.encode('utf8'), u.pname.encode('utf8'), str(u.bday)] for u in ulist]
    f = open('/var/www/lk/logs/remind.csv', 'wb')
    wrtr = csv.writer(f, delimiter=';')
    for r in remind:
        wrtr.writerow(r)
    log_txt.append( "the end")
    return log_txt


def send_remind_list():
    log_txt = [External.objects.get(id = letter).letter_abs  + " \n",]
    
    f = open('/var/www/lk/logs/remind.csv', 'r')
    data = [row for row in csv.reader(f, delimiter=';')]
    log_txt.append(str(len(data)) + " users still to remind \n")
    new_data = []
    for d in data:
        user = UserProfile.objects.filter(sname=d[0], name=d[1], pname=d[2], bday=d[3])[0]
        connection = mail.get_connection()
        ext = External.objects.get(id = letter)
        msg = mail.EmailMessage(ext.letter_abs, ext.letter, "СУНЦ МГУ", [user.user.email,])
        try:
            connection.send_messages([msg,])
        except Exception:
            new_data.append(d)
        else:
            log_txt.append(d[0] + ' ' + d[1] + ' ' + d[2] + " - email sent \n")

    log_txt.append(str(len(new_data)) + " users still to remind \n")

    f = open('/var/www/lk/logs/remind.csv', 'wb')
    wrtr = csv.writer(f, delimiter=';')
    for d in new_data:
        wrtr.writerow(d)
            
    log_txt.append("the end")
    return log_txt

if __name__ == "__main__":
    print 'it is just script'
   # print send_remind_list()
    print 'the end'
       
