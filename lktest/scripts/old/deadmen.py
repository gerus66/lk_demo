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
from django.utils import timezone
from datetime import datetime
from django.core import mail

#--- edge date --------------------------------------------
m = timezone.now().month
y = timezone.now().year
if m >= 6 :
    m = m - 6
else:
    m = m + 6
    y = y - 1
 
s = 'nothing<br>'
i = 0
for u in UserProfile.objects.all():
    if not u.regres_profile.all().count() and not u.answer_profile.all().count() and not u.user.qnans_profile.all().count() and u.user.date_joined < timezone.now().replace(year=y, month=m):
	    
		i = i + 1
		s = s + '<a href="http://lk.internat.msu.ru/admin/auth/user/' + str(u.user.id) + '/delete/">' + u.sname + ' ' + u.name + ' ' + u.pname + '</a> ' + u.user.email + ' ' + u.user.date_joined.strftime("%Y-%m-%d") + '<br>'
s = s + str(i) + '</br>'

s = s + 'only questions on forum</br>'
i = 0
for u in UserProfile.objects.all():
    if not u.regres_profile.all().count() and not u.answer_profile.all().count() and u.user.qnans_profile.all().count() and u.user.date_joined < timezone.now().replace(year=y, month=m):
        
		i = i + 1
		s = s + '<a href="http://lk.internat.msu.ru/admin/auth/user/' + str(u.user.id) + '/delete/">' + u.sname + ' ' + u.name + ' ' + u.pname + '</a> ' + u.user.email + ' ' + u.user.date_joined.strftime("%Y-%m-%d") + '<br>'
s = s + str(i) + '</br>'

s = s + 'answers etc</br>'
i = 0
for u in UserProfile.objects.all():
    if not u.regres_profile.all().count() and u.answer_profile.all().count() and u.user.date_joined < timezone.now().replace(year=y, month=m):
        
		i = i + 1
		s = s + '<a href="http://lk.internat.msu.ru/admin/auth/user/' + str(u.user.id) + '/delete/">' + u.sname + ' ' + u.name + ' ' + u.pname + '</a> ' + u.user.email + ' ' + u.user.date_joined.strftime("%Y-%m-%d") + '<br>'
s = s + str(i) + '</br>'

s = s + 'forms etc</br>'
i = 0
for u in UserProfile.objects.all():
    if u.regres_profile.all().count() and u.user.date_joined < timezone.now().replace(year=y, month=m):
	    
		fl = False
		for rp in u.regres_profile.all():
		    if rp.form.id in [72, 73, 74, 75, 76, 87, 95, 96, 104, 105, 113, 143, 157, 158, 159, 160, 161, 162, 189] :
			    
				fl = True
		
		if not fl:
		    i = i + 1
		    s = s + '<a href="http://lk.internat.msu.ru/admin/auth/user/' + str(u.user.id) + '/delete/">' + u.sname + ' ' + u.name + ' ' + u.pname + '</a> ' + u.user.email + ' ' + u.user.date_joined.strftime("%Y-%m-%d") + '<br>'
s = s + str(i) + '</br>'
 
connection = mail.get_connection()
msg = mail.EmailMessage('deadmen', s, 'Личный Кабинет СУНЦ МГУ <auto@automail.aesc.msu.ru>', ['unforgiven8@yandex.ru',])
msg.content_subtype = "html"
try:
    connection.send_messages([msg,])
except Exception:        
    s = s + "cannot send email"              
else:
    s = s + "email sent"

