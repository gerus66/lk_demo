#!/usr/bin/python
# -*- coding: utf-8 -*-

# delete users that don't activate their profiles for 3 days

import sys
sys.path += ['/var/www/lk']

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'lk.settings'

import django
django.setup()
 
from django.contrib.auth.models import User
from django.utils import timezone

def delete_inactive ():
    y, m, d = timezone.now().year, timezone.now().month, timezone.now().day
    if d > 3 :
        deadline = timezone.now().replace(day = d - 3)
    elif m > 1:
 	    deadline = timezone.now().replace(month = m - 1, day = 28)
    else:
        deadline = timezone.now().replace(year = y - 1, month = 12, day = 28)
    log_txt = ['delete users registered before {0:%d}-{0:%m}-{0:%Y} {0:%H}:{0:%M} and havent activated their profiles yet'.format(deadline),'']
    deleted = 0
    for u in User.objects.filter(is_active=False).order_by('date_joined'):
        if u.date_joined > deadline:
            break
        else:
            log_str = '{0} {1} {2} {3:%Y}-{3:%m}-{3:%d} {3:%H}:{3:%M}'.format(u.profile.all()[0].sname.encode('utf8'), u.profile.all()[0].name.encode('utf8'), u.profile.all()[0].pname.encode('utf8'), u.date_joined)
            u.delete()
            deleted += 1
            log_txt.append(' - '.join([log_str, 'deleted']))
    log_txt.extend(['', '{0} users deleted'.format(deleted), 'the end'])
    return log_txt

if __name__ == "__main__":
    print 'it is just script'
    for d in delete_inactive():
        print d
    print 'the end'
