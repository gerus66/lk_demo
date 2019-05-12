#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
sys.path += ['/var/www/lk']

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'lk.settings'

import django
django.setup()

from django.contrib.auth.models import User
from lkforms.models import Question, Answer, Form
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

def disk(user_id, s, year): 
    u = User.objects.get(id=user_id).profile.all()[0]
    cl = '7'
    f = open('/var/www/lk/media/pdf/' + str(user_id) + '_certificate_disk_' + year + '.pdf', 'w')
    p = canvas.Canvas('/var/www/lk/media/pdf/' + str(user_id) + '_certificate_disk_' + year + '.pdf')
    w, h = A4
    pdfmetrics.registerFont(TTFont('TimesNewRoman', '/var/www/lk/media/media/myfonts/TimesNewRoman.ttf'))
    pdfmetrics.registerFont(TTFont('MonotypeCorsiva', '/var/www/lk/media/media/myfonts/MonotypeCorsiva.ttf'))
    p.drawImage('/var/www/lk/media/media/certificate_disk_' + year + '.jpg', 0, 0, width=w, height=h)
    p.setFont('TimesNewRoman', 17)
    if u.sex == 1:
        p.drawCentredString(w/2, h/2 + 55, 'учащаяся ' + cl + ' класса')
    else:
        p.drawCentredString(w/2, h/2 + 55, 'учащийся ' + cl + ' класса')
    if (len(u.sname) + len(u.name) + len(u.pname)) < 25:
        p.setFont('MonotypeCorsiva', 38)
    elif (len(u.sname) + len(u.name) + len(u.pname)) < 28:
        p.setFont('MonotypeCorsiva', 36)
    else:
        p.setFont('MonotypeCorsiva', 32)
    p.drawCentredString(w/2, 410, u.sname + ' ' + u.name + ' ' + u.pname)
    p.setFont('TimesNewRoman', 17)
    if u.sex == 1:
        p.drawCentredString(w/2, 365, 'успешно выполнила программу')
    else:
        p.drawCentredString(w/2, 365, 'успешно выполнил программу')
    p.drawCentredString(w/2, 344, 'Дистанционных курсов СУНЦ МГУ')
    p.drawCentredString(w/2, 323, s)
    p.showPage()
    p.save()

disk(11667, 'по биологии', '2017')
