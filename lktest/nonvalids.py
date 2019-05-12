#!/usr/bin/python
# -*- coding: utf-8 -*-

# find and delete users without user-profile

import sys
sys.path += ['/var/www/lk']

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'lk.settings'

import django
django.setup()

from lkforms.models import UserProfile
from django.contrib.auth.models import User

def delete_nonvalid():
    log_txt = ['count of Users: {}'.format(User.objects.count()), 'count of UserProfiles: {}'.format(UserProfile.objects.count())]

    if User.objects.count() - UserProfile.objects.count() :
        for u in User.objects.all():
            if not u.profile.all():        
                log_str = '{} {}'.format(u.id, u.username.encode('utf8'))
                u.delete()
                log_txt.append(' - '.join([log_str, 'deleted']))
    log_txt.append('the end')
    return log_txt

if __name__ == "__main__":
    print 'it is just script'
    for d in delete_nonvalid():
        print d
    print 'the end'
    
