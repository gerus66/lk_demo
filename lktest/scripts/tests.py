#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
sys.path += ['/var/www/lk']

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'lk.settings'

import django
django.setup()

from django.contrib.auth.models import User
from lkforms.models import Answer, Question, UserProfile
from lkforum.models import QnAns, Receiver
from django.db.models import Q 

us = User.objects.get(id='17083')
rc = us.receiver_profile.all()
print rc

print 'the end'
