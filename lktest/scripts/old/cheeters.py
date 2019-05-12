#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
sys.path += ['/var/www/lk']

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'lk.settings'

import django
django.setup()
 
from lkforms.models import UserProfile, Form
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime
from django.core import mail

f = Form.objects.get(id='113')
print f.id, f.name, '\n'

n = 0
for frr in f.regres_list.all():
    for urr in frr.user.regres_profile.all():
        if urr.form.id in [72, 73, 74, 75, 76, 87, 95, 96, 104, 105, 143, 157, 158, 159, 160, 161, 162, 189]:
            print urr.form.id, urr.form.name, '\n', urr.user.id, urr.user.sname, urr.user.name, urr.user.pname, '\n'
            n = n + 1

print 'all - ', n
