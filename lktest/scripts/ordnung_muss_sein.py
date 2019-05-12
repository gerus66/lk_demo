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
from lkforms.views import base_forms

print base_forms

valid_doubles = [980, 5137, 1126, 3007, 1164, 2783, 2260, 3047, 3224, 5486, 3918, 4833, 7651, 3271, 3023, 7069, 7241, 10924, 4956, 10283, 9112, 8969]

if not User.objects.count() - UserProfile.objects.count() == 0:
    s = 'wrong profiles exist<br>'
else:
    s = str(User.objects.count()) + '<br>'

s = s + '<br>doubles<br>'
for u in UserProfile.objects.all():
    if UserProfile.objects.filter(name=u.name, sname=u.sname, pname=u.pname).count() != 1 and u.id not in valid_doubles:
        s = s + '<a href="http://lk.internat.msu.ru/admin/lkforms/userprofile/' + str(u.id) + '/">' + u.sname + ' ' + u.name + ' ' + u.pname + '</a> ' + u.user.email + '<br>'
		
m = timezone.now().month
y = timezone.now().year		
if m >= 6 :
    m = m - 6
else:
    m = m + 6
    y = y - 1

s = s + '<br>only questions on forum<br>'
for u in UserProfile.objects.all():
    if not u.regres_profile.all().count() and not u.answer_profile.all().count() and u.user.qnans_profile.all().count() and u.user.date_joined < timezone.now().replace(year=y, month=m):
		s = s + '<a href="http://lk.internat.msu.ru/admin/auth/user/' + str(u.user.id) + '/delete/">' + u.sname + ' ' + u.name + ' ' + u.pname + '</a> ' + u.user.email + ' ' + u.user.date_joined.strftime("%Y-%m-%d") + '<br>'

s = s + '<br>answers etc<br>'
for u in UserProfile.objects.all():
    if not u.regres_profile.all().count() and u.answer_profile.all().count() and u.user.date_joined < timezone.now().replace(year=y, month=m):
		s = s + '<a href="http://lk.internat.msu.ru/admin/auth/user/' + str(u.user.id) + '/delete/">' + u.sname + ' ' + u.name + ' ' + u.pname + '</a> ' + u.user.email + ' ' + u.user.date_joined.strftime("%Y-%m-%d") + '<br>'

s = s + '<br>forms etc<br>'
for u in UserProfile.objects.all():
    if u.regres_profile.all().count() and u.user.date_joined < timezone.now().replace(year=y, month=m):
	    
		fl = False
		for rp in u.regres_profile.all():
		    if rp.form.id in [72, 73, 74, 75, 76, 87, 95, 96, 104, 105, 113, 143, 157, 158, 159, 160, 161, 162, 189] :
			    
				fl = True
		
		if not fl:
		    s = s + '<a href="http://lk.internat.msu.ru/admin/auth/user/' + str(u.user.id) + '/delete/">' + u.sname + ' ' + u.name + ' ' + u.pname + '</a> ' + u.user.email + ' ' + u.user.date_joined.strftime("%Y-%m-%d") + '<br>'
 
connection = mail.get_connection()
msg = mail.EmailMessage('ordnung muss sein', s, 'Личный Кабинет СУНЦ МГУ <auto@automail.aesc.msu.ru>', ['unforgiven8@yandex.ru',])
msg.content_subtype = "html"
try:
    connection.send_messages([msg,])
except Exception:        
    s = s + "cannot send email"              
else:
    s = s + "email sent"

print 'end'
