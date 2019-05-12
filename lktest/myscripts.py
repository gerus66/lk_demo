#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
sys.path += ['/var/www/lk']

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'lk.settings'

import django
django.setup()

from lkforms.models import External, RegRes, Question, Form, FmQn, Answer, UserProfile
from django.contrib.auth.models import User
from django.db.models import Q
from django.utils import timezone
from django.core import mail
import csv
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


def make_userlist(key, fm_ids):   # list of USERS who:
    if key == 'passed':  # ..passed any form from 'fm_ids' ones.
        ulist = [r.user.user for r in RegRes.objects.filter(form__id__in=fm_ids, short_result='1')]
        ulist = list(set(ulist))
    else:
        print 'wrong key'
    return ulist

def send_email(ext_id, key, fm_ids):
    log = open('/var/www/lk/logs/'+str(timezone.now().month)+str(timezone.now().day)+str(timezone.now().minute)+str(timezone.now().second)+'.log', 'wb')
    
    ext = External.objects.get(id=ext_id)   # letter to send 
    ulist = make_userlist(key, fm_ids)

    log_txt = ['send info email ' + ' - ' + ext.letter_abs.encode('utf8') + '\n',]    
    log_txt.append(str(len(ulist)) + '\n')
    
    for u in ulist:
        log_str = u.profile.all()[0].sname.encode('utf8') + ' ' + u.profile.all()[0].name.encode('utf8') + ' ' + u.profile.all()[0].pname.encode('utf8') + ' ' + u.email.encode('utf8')
        connection = mail.get_connection()
        msg = mail.EmailMessage(ext.letter_abs, ext.letter + '\n--\n\nThis letter is generated automatically. Responses are not processed.', 'Личный Кабинет СУНЦ МГУ <auto@automail.aesc.msu.ru>', [u.email,])
        try:
            connection.send_messages([msg,])
        except Exception:        
            log_str = log_str + " - error, cannot send email \n"               
        log_str = log_str + ' - email sent \n'
        log_txt.append(log_str)
    
    log_txt.append('the end')
    log.writelines(log_txt)
    return 1
    
     
def send_info_email(ext_id, fm_ids):
    log = open('/var/www/lk/logs/'+str(timezone.now().month)+str(timezone.now().day)+str(timezone.now().minute)+str(timezone.now().second)+'.log', 'wb')
    
    ext = External.objects.get(id=ext_id)   # letter to send 
    qn = Question.objects.get(id=778)   # question if member want to receive a mail

    log_txt = ['send info email ' + ' - ' + ext.letter_abs.encode('utf8') + '\n',]    
    log_txt.append(str(RegRes.objects.filter(form__id__in=fm_ids, is_checkin=True).count()) + '\n')
    
    for rr in RegRes.objects.filter(form__id__in=fm_ids, is_checkin=True) :
        log_str = rr.user.sname.encode('utf8') + ' ' + rr.user.name.encode('utf8') + ' ' + rr.user.pname.encode('utf8')
        if rr.user.answer_profile.filter(question=qn)[0].answer[0:2] == 'ye' :
            connection = mail.get_connection()
            msg = mail.EmailMessage(ext.letter_abs, ext.letter + '\n--\n\nThis letter is generated automatically. Responses are not processed.', 'Личный Кабинет СУНЦ МГУ <auto@automail.aesc.msu.ru>', [rr.user.user.email,])
            try:
                connection.send_messages([msg,])
            except Exception:        
                log_str = log_str + " - error, cannot send email"               
            log_str = log_str + ' - email sent'
        else:
            if rr.user.answer_profile.filter(question=qn)[0].answer[0:2] == 'no' :
                log_str = log_str + ' - dont want to receive mails'
            else:
                log_str = log_str + ' - error, unknown answer ' + rr.user.answer_profile.filter(question=qn)[0].answer
        log_str = log_str + '\n'
        log_txt.append(log_str)
    
    log_txt.append('the end')
    log.writelines(log_txt)
    return 1



def check_bio():
    form = Form.objects.get(id=199)   # IO 7-8 bio 2 stage
    f = open('/var/www/lk/media/answers/bio_answers.csv', 'r')
    data = [row for row in csv.reader(f, delimiter=';')]
  
    err = []    
    for i in range(4,len(data[0])-1):  
        qn = Question.objects.filter(id=data[0][i][:data[0][i].find('.')])
        if not qn:
            err.append(data[0][i][:data[0][i].find('.')] + ' question not exist')
        elif not FmQn.objects.filter(form=form, question=qn[0]):
            err.append(data[0][i][:data[0][i].find('.')] + ' question not from this form')
            
    if err:
        data.append(err)  
    else:
        for rr in RegRes.objects.filter(form=form, is_checkin=True): 
            sum = 0
            ss = [rr.user.sname.encode('utf8'), rr.user.name.encode('utf8'), rr.user.pname.encode('utf8'), str(rr.user.bday)]
            for i in range(4,len(data[0])):
                ans = Answer.objects.filter(user=rr.user, question=Question.objects.filter(id=data[0][i][:data[0][i].find('.')])[0])
                if not ans:    # no answers
                    ss.append('(0)')
                else:
                    user_ans = ans[0].answer.lower().encode('utf8').strip()
                    right_ans = data[1][i].decode('utf8').lower().encode('utf8').strip()
                    # if i == 4:
                     #   user_ar = user_ans.split(',')
                     #   user_ar = user_ar[1:len(user_ar)-1]                   
                      #  right_ar = right_ans.split(',')
                      #  right_ar = right_ar[1:len(right_ar)-1]
                      #  one_sum = 0
                     #   print 'right_ar ', right_ar
                      #  print 'user_ar ', user_ar
                      #  for k in user_ar:
                      #      if k.strip() in right_ar:
                       #        # print k 
                       #         one_sum = one_sum + 2
                           # else:
                             #   print 'wrong' + k 
                      #  ss.append(user_ans + ' (' + str(one_sum) + ')')
                      #  sum = sum + one_sum
                  #  if i == 5:    # 2nd question
                    user_ar = user_ans.split('|')
                    user_ar = user_ar[1:len(user_ar)-1]                   
                    right_ar = right_ans.split('|')
                    right_ar = right_ar[1:len(right_ar)-1]
                    one_sum = 0
                    for k in range(1,11):
                  #      if (k < 10):
                   #         sk = '0' + str(k);
                    #    else:
                        sk = str(k);
                        if  right_ar.count(sk) and user_ar.count(sk) or not right_ar.count(sk) and not user_ar.count(sk) :
                             #   print k, ' | ', right_ar, ' | ', user_ar, ' +5' 
                            one_sum = one_sum + 2
                        if  right_ar.count(sk) and not user_ar.count(sk) or not right_ar.count(sk) and user_ar.count(sk) :
                             #   print k, ' | ', right_ar, ' | ', user_ar, ' -5' 
                            one_sum = one_sum - 2
                    ss.append(user_ans + ' (' + str(one_sum) + ')')
                    sum = sum + one_sum
                  #  if i in range(6, 17):
                   #     if user_ans == right_ans:
                    #        sum = sum + 3
                    #        ss.append(user_ans + '(3)')
                     #   else:
                    #        ss.append(user_ans + '(0)')
                 #   if i == 17:   # 5th question
                  #      user_ar = user_ans.split('|')
                   #     user_ar = user_ar[1:len(user_ar)-1]                   
                    #    right_ar = right_ans.split('|')
                    #    right_ar = right_ar[1:len(right_ar)-1]
                     #   one_sum = 0
                      #  for k in range(1,6):
                       #     if  right_ar.count(str(k)) and user_ar.count(str(k)) or not right_ar.count(str(k)) and not user_ar.count(str(k)) :
                        #        one_sum = one_sum + 3
                         #   if  right_ar.count(str(k)) and not user_ar.count(str(k)) or not right_ar.count(str(k)) and user_ar.count(str(k)) :
                          #      one_sum = one_sum - 3
                      #  ss.append(user_ans + ' (' + str(one_sum) + ')')
                       # sum = sum + one_sum
            ss.append(str(sum))
            data.append(ss)
        data.append(['no errors'])
            
    data.append(['was checked',timezone.now().strftime("%Y-%m-%d %H:%M")])
    f = open('/var/www/lk/media/answers/bio_checked.csv', 'wb')
    wrtr = csv.writer(f, delimiter=';')
    for d in data:
        wrtr.writerow(d)


check_bio() 
