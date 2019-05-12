#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
sys.path += ['/var/www/lk']

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'lk.settings'

import django
django.setup()

from django.contrib.auth.models import User
from lkforms.models import Form, UserProfile
#from lkforum.models import QnAns, Receiver
#from django.db.models import Q
import csv

u1 = User.objects.get(id = 21420)

forms = Form.objects.filter(theme = '14')
for f in forms:
    f.reader.add(u1)
   

print 'the end'
