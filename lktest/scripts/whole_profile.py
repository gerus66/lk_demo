#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
sys.path += ['/var/www/lk']

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'lk.settings'

import django
django.setup()

from lkforms.models import UserProfile

u = UserProfile.objects.get(id=3430)

print str(u.id) + u.sname.encode('utf8') + u.name.encode('utf8') + u.pname.encode('utf8')
print str(u.regres_profile.count()) + ' regres'
print str(u.answer_profile.count()) + ' answer'
print str(u.archregres_profile.count()) + ' archive regres'
print str(u.archanswer_profile.count()) + ' archive answer'
print str(u.user.own_forms.count()) + ' own forms'
print str(u.user.edit_forms.count()) + ' edit forms'
print str(u.user.read_forms.count()) + ' read forms'
print str(u.user.use_forms.count()) + ' use forms'
print str(u.user.own_external.count()) + ' own external'
print str(u.user.receiver_profile.count()) + ' receiver'
print str(u.user.qnans_profile.count()) + ' asked qns'
print str(u.user.own_mforms.count()) + ' own mforms'
print str(u.user.edit_mforms.count()) + ' edit mforms'
print str(u.user.read_mforms.count()) + ' read mforms'
print str(u.user.own_mqns.count()) + ' own mqns'
print str(u.user.req_list.count()) + ' requests'
print str(u.user.mod_list.count()) + ' moderations'
print str(u.user.qreq_list.count()) + ' qrequests'
print str(u.user.qmod_list.count()) + ' qmoderations'


print 'the end'
