#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
sys.path += ['/var/www/lk']

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'lk.settings'

import django
django.setup()
 
from lkforms.models import UserProfile
from django.contrib.auth.models import User
from django.core import mail

s = '' 
for u in UserProfile.objects.all():
    if UserProfile.objects.filter(name=u.name, sname=u.sname, pname=u.pname).count() != 1 and u.id not in []:
        s = s + '<a href="http://lk.internat.msu.ru/admin/lkforms/userprofile/' + str(u.id) + '/">' + u.sname + ' ' + u.name + ' ' + u.pname + '</a> ' + u.user.email + '<br>'

connection = mail.get_connection()
msg = mail.EmailMessage('doubles', s, 'Личный Кабинет СУНЦ МГУ <auto@automail.aesc.msu.ru>', ['unforgiven8@yandex.ru',])
msg.content_subtype = "html"
try:
    connection.send_messages([msg,])
except Exception:        
    s = s + "cannot send email"              
else:
    s = s + "email sent"
