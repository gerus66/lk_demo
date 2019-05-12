#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
sys.path += ['/var/www/lk']

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'lk.settings'

import django
django.setup()



from django.utils import timezone
from datetime import datetime
from django.contrib.auth.models import User, Group
from lkforms.models import Form, RegRes, Answer, ArchiveRegRes, UserProfile, Question, ArchiveAnswer, External, FmQn
import csv

def check_test(filename):
    form = Form.objects.get(id=filename[:filename.find('_')])
    f = open(filename, 'r')
    data = [row for row in csv.reader(f, delimiter=';')]
    if len(data) > 5:      
        for i in range(5,len(data)):
            data.pop()
    
    sumpoints = 0
    for i in range(4,len(data[0])):  
        sumpoints = sumpoints + int(data[4][i])
    
    err = []    
    if len(data[1]) == len(data[0]):  
        data[1] = data[1] + ['points (' + str(sumpoints) + ')', '% (100)']
        add = True
    else:
        add = False

    for i in range(4,len(data[0])):  
        qn = Question.objects.filter(id=data[0][i][:data[0][i].find('.')])
        if not qn:
            err.append(data[0][i][:data[0][i].find('.')] + ' question not exist')
        elif not FmQn.objects.filter(form=form, question=qn[0]):
            err.append(data[0][i][:data[0][i].find('.')] + ' question not from this form')
        elif add: 
            data[1].append(data[0][i] + ' accepted')

    if err:
        data.append(err)  
    else:
        for rr in RegRes.objects.filter(form=form, is_checkin=True): 
            sum = 0
            ss = [rr.user.sname.encode('utf8'), rr.user.name.encode('utf8'), rr.user.pname.encode('utf8'), str(rr.user.bday)]
            add_ss = []
            for i in range(4,len(data[0])):
                ans = Answer.objects.filter(user=rr.user, question=Question.objects.filter(id=data[0][i][:data[0][i].find('.')])[0])
                if not ans:
                    ss.append('')
                    add_ss.append('')
                else:
                    user_ans = ans[0].answer.encode('utf8')
                    modify_user_ans = user_ans.decode('utf8').lower().encode('utf8') 
                    modify_user_ans = modify_user_ans.replace(',','.').strip() 
                    modify_user_ans = modify_user_ans.replace('ё', 'е') 
                    j = 1
                    fll = False
                    while (j < 4) and not fll :
                        right_ans = data[j][i].decode('utf8').lower().encode('utf8')  
                        right_ans = right_ans.replace(',','.').strip() 
                        right_ans = right_ans.replace('ё', 'е') 
                        new_modify_user_ans = modify_user_ans
                        if right_ans[0] == '_':   
                            right_ans = right_ans[1:]
                            right_ans = right_ans.replace(' ','').replace(';','')
                            new_modify_user_ans = modify_user_ans.replace(' ','').replace(';','')
                        if right_ans[0] == '*':    
                            right_ans = right_ans[1:]
                            fl = False
                            while not fl and len(new_modify_user_ans) != 0 :
                                if new_modify_user_ans[0].isdigit() or new_modify_user_ans[0] == '-':
                                    fl = True
                                else:
								    new_modify_user_ans = new_modify_user_ans[1:]  
                        if right_ans[-1] == '#' or right_ans[-1] == '$':   
                            if len(new_modify_user_ans) > (len(right_ans)-1) and ( right_ans[-1] == '#' or right_ans[-1] == '$' and not new_modify_user_ans[len(right_ans)-1].isdigit() and not new_modify_user_ans[len(right_ans)-1] == '.' ):
                                new_modify_user_ans = new_modify_user_ans[:len(right_ans)-1]
                            right_ans = right_ans[:-1]
                        if new_modify_user_ans == right_ans:
                            fll = True
                        j = j + 1
                    if fll:    
                        ss.append(data[4][i])
                        sum = sum + int(data[4][i])
                        add_ss.append(user_ans)
                    else:
                        ss.append(user_ans + ' ' )
                        add_ss.append('')
            ss = ss + [sum, sum/sumpoints*100]
            data.append(ss+add_ss)
        data.append(['no errors'])
            
    data.append(['new version was checked',timezone.now().strftime("%Y-%m-%d %H:%M")])
    f = open(filename, 'wb')
    wrtr = csv.writer(f, delimiter=';')
    for d in data:
        wrtr.writerow(d)
        

check_test('148_chem_89.csv')
