#!/usr/bin/python
# -*- coding: utf-8 -*-

# [Form, Status]: set status of Form (by id) to Status (0, 1, True, False)

import sys
sys.path += ['/var/www/lk']

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'lk.settings'

import django
django.setup()

from lkforms.models import Form

(n, form_id, active_status, ) = sys.argv

f = Form.objects.get(id=form_id)
print f.name

status = f.is_active

if active_status == 'False' or active_status == '0' :
    status = 0
else:
    if active_status == 'True' or active_status == '1' :
        status = 1
    else:
        print 'wrong status'

f.is_active = status
f.save()
print f.is_active

print 'the end'
