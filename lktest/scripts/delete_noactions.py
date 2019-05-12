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

def delete_noactions():
    m = timezone.now().month
    y = timezone.now().year		
    if m >= 6 :
        m = m - 6
    else:
        m = m + 6
        y = y - 1

   # log = open('/var/www/lk/logs/'+str(timezone.now().month)+str(timezone.now().day)+str(timezone.now().minute)+str(timezone.now().second)+'.log', 'wb')
    log_txt = ['delete inactive users(for half of year) \n',]

    ext = External.objects.get(id=105)    # letter 
        
    i=0
    for u in UserProfile.objects.order_by('sname'):
        if ( u.regres_profile.count() + u.answer_profile.count() + u.archregres_profile.count() + u.archanswer_profile.count() + u.user.own_forms.count() + u.user.edit_forms.count() + u.user.read_forms.count() + u.user.use_forms.count() + u.user.own_external.count() + u.user.receiver_profile.count() + u.user.qnans_profile.count() + u.user.own_mforms.count() + u.user.edit_mforms.count() + u.user.read_mforms.count() + u.user.own_mqns.count() + u.user.req_list.count() + u.user.mod_list.count() + u.user.qreq_list.count() + u.user.qmod_list.count() ) == 0 and u.user.date_joined < timezone.now().replace(year=y, month=m):
            log_str = u.sname.encode('utf8') + ' ' + u.name.encode('utf8') + ' ' + u.pname.encode('utf8')
            connection = mail.get_connection()
            msg = mail.EmailMessage(ext.letter_abs, ext.letter + '\n--\n\nThis letter is generated automatically. Responses are not processed.', 'Личный Кабинет СУНЦ МГУ <auto@automail.aesc.msu.ru>', [u.user.email,])
            try:
                connection.send_messages([msg,])
            except Exception:        
                log_str = log_str + " - error, cannot send email"                
            else:
                log_str = log_str + " - email sent"  
                u.user.delete()
                i = i+1
                log_str = log_str + ' - deleted'
            log_str = log_str + '\n'
            log_txt.append(log_str)
    return log_txt	         

for d in delete_inactive():
    print d
print 'the end'

       
