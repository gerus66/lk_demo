#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
sys.path += ['/var/www/lk']

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'lk.settings'

import django
django.setup()
 
import csv
from lkforms.models import Form, Answer

m0 = Form.objects.get(id=163)  # заявка команды
m_accomp = Form.objects.get(id=164)  # данные о сопровождающем
m_main = [ Form.objects.get(id=i) for i in [165,169,170,171,177] ]  # данные об участниках 1-5
#m_extra = [ Form.objects.get(id=i) for i in [167,168] ]  # дополнительные данные

def get_ans(form):    # ответы из формы form в виде списка
    line = []
    for fmqn in form.fmqn_fmlist.order_by('number'):
        if Answer.objects.filter(user=rr.user, question=fmqn.question):
            line.append( Answer.objects.filter(user=rr.user, question=fmqn.question)[0].answer.encode('utf-8') )
        else:
            line.append( '---' )
    return line
    
data = []
first = ( [ str(qn.number)+'.'+qn.question.name.encode('utf-8') for qn in m0.fmqn_fmlist.order_by('number') ] +
          [ str(qn.number)+'.'+qn.question.name.encode('utf-8') for qn in m_main[0].fmqn_fmlist.order_by('number') ] +
          [ str(qn.number)+'.'+qn.question.name.encode('utf-8') for qn in m_accomp.fmqn_fmlist.order_by('number')] )
data.append(first)

for rr in m0.regres_list.all():
    for m in m_main:
        if m.regres_list.filter(user=rr.user):
            data.append( get_ans(m0) + get_ans(m) + get_ans(m_accomp) )       

f = open('/var/www/lk/media/data/mm.csv', 'wb')
wrtr = csv.writer(f, delimiter=';')
for d in data:
    wrtr.writerow(d)

print 'the end'

