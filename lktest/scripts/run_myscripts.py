#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
sys.path += ['/var/www/lk']

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'lk.settings'

import django
django.setup()

from lktest.myscripts import send_info_email, check_bio, send_email 

# 10 - start of IO 2 stage
# 11 - end of IO 2 stage
# 12 - start of IO 3 stage
# 13 - diploms
# 56, 57 - IO 7-8 classes
# 58, 59 - IO 9-10 classes
#send_info_email(11, [56, 57])  

#send_email(12, 'passed', [203,227])

#diplom(9938, 'pdf_phys1 Диплом победителя по физике', '2017')

#anketa(14014, '272')

#make_userlist('passed', [199,224])

check_bio()

print 'the end'

