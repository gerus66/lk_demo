#from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.utils import timezone
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User, Group
from lkforms.models import Form, RegRes, Answer, ArchiveRegRes, UserProfile, Question, ArchiveAnswer, External, FmQn
from lkforms import urls
from lkforum.models import Receiver, QnAns
from lkmoderation.models import Request, QRequest
import csv
from django.db.models import Q   
from django.core import mail
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from django.utils.translation import ugettext as _

 
base_forms = [72, 73, 74, 75, 76, 87, 95, 96, 113, 143, 157, 158, 159, 160, 161, 162, 189, 262]

# 8, 68, 83, 84, 234 - disk
# 135, 64, 65, 131 - zash last year
# 258, 254, 253, 252, 251 - zash this year
all_cdo = [8, 68, 83, 84, 234, 135, 64, 65, 131]
# 190-194 - IO_9_10
# 229-233 - IO_7_8
all_io = [190, 191, 192, 193, 194, 229, 230, 231, 232, 233]

def administrator_check(user):
    return Group.objects.get(id=2) in user.groups.all()
    
def activation_check(user):
    return user.is_active
  
def avaliable_check(user, form):
    fl = True
    if form.aif.all():
        fl = False
        for fm in form.aif.all():
            if RegRes.objects.filter(user=user).filter(form=fm).filter(is_checkin=True):
                fl = True
    if form.unaif.all():
        for fm in form.unaif.all():
            if RegRes.objects.filter(user=user).filter(form=fm).filter(is_checkin=True):
                fl = False
    if form.aifpass.all() and fl:
        fl = False
        for fm in form.aifpass.all():
            if RegRes.objects.filter(user=user).filter(form=fm).filter(short_result=1):
                fl = True
    if form.aifres.all() and fl:
        fl = False
        for fm in form.aifres.all():
            if RegRes.objects.filter(user=user).filter(form=fm).filter(short_result=3):
                fl = True  
    if form.start_time and form.finish_time:
        if form.start_time < timezone.now() and form.finish_time > timezone.now():
            form.is_active = 1
        if form.start_time > timezone.now() or form.finish_time < timezone.now():
            form.is_active = 0
        form.save() 
    return fl and form.is_active           

    
def back(req):
    try: 
        req.META['HTTP_REFERER']
    except KeyError:
        return '/'
    else:
        return req.META['HTTP_REFERER']   
    

@user_passes_test(activation_check)    
def forms(req):
    for fm in Form.objects.filter(start_time__lt=timezone.now(), finish_time__gt=timezone.now()):
        fm.is_active = 1
        fm.save()
    for fm in Form.objects.filter(start_time__gt=timezone.now(), finish_time__lt=timezone.now()):
        fm.is_active = 0
        fm.save()    
    br = []
    for rr in RegRes.objects.filter(user=req.user.profile.all()[0]):
        if rr.form.id in base_forms:
            br.append(rr.form) 
    thms = []
    for i in [1,20,14,16,17,18,21,22]:
        thms.append([form for form in Form.objects.filter(user_theme__id=i) if avaliable_check(req.user.profile.all()[0], form)])   
    return render(req, 'lkforms/forms.html', {'thms': thms, 'fmchecks': [rr.form for rr in RegRes.objects.filter(user=req.user.profile.all()[0], is_checkin=True)], 'br': br})
    

@user_passes_test(activation_check)    
def form(req, form_id):
    user = req.user.profile.all()[0]   
    form = Form.objects.get(id=form_id)  
    txt = ''     
    fl = True  
    wq = []    
    if avaliable_check(user, form):
        qns = [fq.question for fq in form.fmqn_fmlist.filter(is_priv=False).order_by('number')]
        if req.POST:           
            for q in qns:
                if q.multi_vars:
                    if req.POST.getlist(str(q.id)):
                        a = Answer.objects.filter(user=user, question=q)
                        if a:
                            a[0].answer='|' + '|'.join(req.POST.getlist(str(q.id))) + '|'
                            a[0].save()
                        else:
                            Answer.objects.create(user=user, question=q, answer='|' + '|'.join(req.POST.getlist(str(q.id)))+ '|') 
                        txt = _(u'Изменения сохранены. <br><a href="/lk/forms/"> Вернуться к списку форм</a>')
                    else:
                        if q.not_blank:
                            fl = False
                            wq.append(q)
                        else:
                            if Answer.objects.filter(user=user, question=q):
                                Answer.objects.filter(user=user, question=q)[0].delete()
                else:
                    if req.POST.get(str(q.id), ''):
                        a = Answer.objects.filter(user=user, question=q)
                        if a:
                            a[0].answer=req.POST.get(str(q.id), '')
                            a[0].save()
                        else:
                            Answer.objects.create(user=user, question=q, answer=req.POST.get(str(q.id), ''))
                        txt = _(u'Изменения сохранены. <br><a href="/lk/forms/"> Вернуться к списку форм</a>')
                    else:
                        if q.not_blank:
                            fl = False
                            wq.append(q)
                        else:
                            if Answer.objects.filter(user=user, question=q):
                                Answer.objects.filter(user=user, question=q)[0].delete()
            if fl:
                if RegRes.objects.filter(user=user).filter(form=form):
                    rr = RegRes.objects.filter(user=user).filter(form=form)[0]
                    rr.is_checkin = True
                    rr.save()
                else:
                    RegRes.objects.create(user=user, form=form, is_checkin=True)
                if form.result and form.last_res_publication:
                    make_result(form.result.name[form.result.name.find('/')+1:])
           #     if form_id=='288' or form_id=='289' or form_id=='290' or form_id=='294' or form_id=='295' or form_id=='296':
            #        anketa(req.user.id, form_id)
            else:
                txt = _(u'Вы не ответили на обязательные вопросы (обязательные вопросы отмечены *)')
        if txt == '':
            txt = _(u'Заполните форму и нажмите "Сохранить".<br>Обязательные вопросы отмечены *.')	
        return render(req, 'lkforms/form.html',{'form': form, 'qns': qns, 'wq': wq, 'txt': txt})
    else:
        return HttpResponseRedirect(back(req))
    
@user_passes_test(activation_check)    
def reverse(req, form_id):
    form = Form.objects.get(id=form_id)
    if avaliable_check(req.user.profile.all()[0], form) and not form.not_reversed:
        rr = RegRes.objects.filter(user=req.user.profile.all()[0], form=form)[0]
        if rr.short_result == 0 and rr.detail_result == '' and rr.private_result == '':
            rr.delete()
        else:
            rr.is_checkin = False
            rr.save()
    return HttpResponseRedirect(back(req))
    
@user_passes_test(activation_check)
def result (req, form_id):
    fl = False
    rr = RegRes.objects.filter(user=req.user.profile.all()[0]).filter(form=Form.objects.get(id=form_id))
    if rr:
        if rr[0].short_result <> 0 or rr[0].detail_result <> '':
            r = rr[0]
            fl = True
    if not fl:
        arr = ArchiveRegRes.objects.filter(user=req.user.profile.all()[0]).filter(form=Form.objects.get(id=form_id))
        if arr:
            if arr[0].short_result <> 0 or arr[0].detail_result <> '':
                r = arr[0]
    return render(req, 'lkforms/result.html', {'r': r})

@user_passes_test(activation_check)    
def structure(req):
    return render(req, 'lkforms/structure.html', {'fms': Form.objects.filter(is_active=1),})

@user_passes_test(activation_check)                
def download(req, file_type, file_name):
    if file_type == 'txt':
        fm = Form.objects.get(id=file_name[:file_name.find('.')])
        fm.make_txt()
    elif file_type == 'pdf':
        file_name = str(req.user.id) + '_' + file_name + '.pdf'
    f = open('/var/www/lk/media/' + file_type + '/' + file_name, 'rb')
    return HttpResponse(f, content_type='application/octet-stream')
    
def make_structure():
    file = [['Форма', 'Доступна, если','Недоступна, если'],]
    for fm in Form.objects.filter(is_active=1):
        line = []
        line.append(fm.name.encode('utf8'))
        fl = True
        txt = ''
        for f in fm.aif.all():
            if not fl:
                txt = txt + '\n' + 'или '
            txt = txt + f.name.encode('utf8')
            fl = False
        fl = True
        for f in fm.aifpass.all():
            if fl and fm.aif.all():
                txt = txt + '\n' + 'и' + '\n'
            if not fl:
                txt = txt + '\n' + 'или '
            txt = txt + f.name.encode('utf8') + ' - пройдено успешно' 
            fl = False
        fl = True
        for f in fm.aifres.all():
            if fl and fm.aif.all() or fl and fm.aifpass.all():
                txt = txt + '\n' + 'и' + '\n'
            if not fl:
                txt = txt + '\n' + 'или '
            txt = txt + f.name.encode('utf8') + ' - в резерве'
            fl = False
        line.append(txt)
        txt = ''
        fl = True
        for f in fm.unaif.all():
            if not fl:
                txt = txt + '\n' + 'или '
            txt = txt + f.name.encode('utf8')
            fl = False
        line.append(txt)
        file.append(line)
    f = open('/var/www/lk/media/structure/structure.csv', 'wb')
    wrtr = csv.writer(f, delimiter=';')
    for line in file:
        wrtr.writerow(line)

def code_to_newcode(data, code, newcode):   
    for i in range(0,len(data)):
        for j in range(0,len(data[i])):
            data[i][j] = str(data[i][j]).decode(code).encode(newcode)   
    return data            
 
def user_identify(sname, name, pname, bday): 
    if UserProfile.objects.filter(sname=sname, name=name, pname=pname, bday=bday):
        if User.objects.filter(username=UserProfile.objects.filter(sname=sname, name=name, pname=pname, bday=bday)[0].user).filter(is_active=1):
            return 'ok'
        else:
            return 'profile not active'
    else: 
        return 'profile not exist'

def ya_user_identify(sname, name, pname, bday): 
    if sname != '' and name != '' and pname != '' and bday != '':
        return [user_identify(sname, name, pname, bday), '', '', '', '', '']
    elif sname != '' and name != '':
        ar = ['nothing', '', '', '', '', '']
        for u in UserProfile.objects.filter(sname=sname, name=name):
            if (pname.lower() == u.pname.encode('utf8').lower() or pname == '') and (bday.lower() == str(u.bday).lower() or bday == '') :
                ar[0] = 'found'
                if ar[1] == '':
                    ar[1] = u.sname.encode('utf8')
                else:
                    ar[1] = ar[1] + '\n' + u.sname.encode('utf8')
                if ar[2] == '':
                    ar[2] = u.name.encode('utf8')
                else:
                    ar[2] = ar[2] + '\n' + u.name.encode('utf8')
                if ar[3] == '':
                    ar[3] = u.pname.encode('utf8')
                else:
                    ar[3] = ar[3] + '\n' + u.pname.encode('utf8')
                if ar[4] == '':
                    ar[4] = str(u.bday)
                else:
                    ar[4] = ar[4] + '\n' + str(u.bday)
                if ar[5] == '':
                    ar[5] = u.user.email.encode('utf8')
                else:
                    ar[5] = ar[5] + '\n' + u.user.email.encode('utf8')
        return ar
            
            
def set_external(req, filename, label):
    f = open('/var/www/lk/media/external/' + str(filename), 'r')
    ext = External.objects.get(id=filename[:filename.find('_')])
    if ext.is_utf: 
        data = [row for row in csv.reader(f, delimiter=';')]
    else:
        data = code_to_newcode([row for row in csv.reader(f, delimiter=';')], 'cp1251', 'utf8')
    er = ''
    if label == 'set':
        qns = []
        for j in range(4,len(data[0])):
            if str(data[0][j][:3]) <> 'res':
                try: 
                    int(data[0][j][0:data[0][j].find('.')])
                except ValueError:
                    er = er + '\n' + 'invalid format - ' + str(data[0][j])
                else:
                    if Question.objects.filter(id=data[0][j][0:data[0][j].find('.')]):
                        fl = False
                        for fq in Question.objects.get(id=data[0][j][0:data[0][j].find('.')]).fmqn_qnlist.all():
                            if fq.form.owner == req.user or req.user in fq.form.editor.all() or req.user.is_superuser:
                                fl = True
                        if fl:
                            qns.append(j)
                        else:
                            er =  er + '\n' + 'access denied - ' + str(data[0][j]) 
                    else:
                        er =  er + '\n' + 'question not found - ' + str(data[0][j])        
    for i in range(1,len(data)):
        if label == 'find':
            ar = ya_user_identify(data[i][0], data[i][1], data[i][2], data[i][3])
            if ar: 
                data[i] = data[i] + ar
        elif user_identify(data[i][0], data[i][1], data[i][2], data[i][3]) == 'ok':
            if label == 'set':
                for j in qns:
                    a = Answer.objects.filter(user=UserProfile.objects.filter(sname=data[i][0], name=data[i][1], pname=data[i][2], bday=data[i][3])[0]).filter(question=Question.objects.get(id=data[0][j][0:data[0][j].find('.')]))
                    if data[i][j] == '':  
                        if a:
                            a[0].delete()                            
                    else:
                        if a:
                            a[0].answer = data[i][j]
                            a[0].save()
                        else:
                            Answer.objects.create(user=UserProfile.objects.filter(sname=data[i][0], name=data[i][1], pname=data[i][2], bday=data[i][3])[0], question=Question.objects.get(id=data[0][j][0:data[0][j].find('.')]), answer=data[i][j])
                data[i].append(user_identify(data[i][0], data[i][1], data[i][2], data[i][3]))
            elif label == 'send':
                connection = mail.get_connection()
                ext = External.objects.get(id=filename[:filename.find('_')])
                up = UserProfile.objects.filter(sname=data[i][0], name=data[i][1], pname=data[i][2], bday=data[i][3])[0]
                add_email = Question.objects.get(id=30)
                if up.answer_profile.filter(question=add_email):
                    msg = mail.EmailMessage(ext.letter_abs, ext.letter + '\n--\n\nThis letter is generated automatically. Responses are not processed.', 'Личный Кабинет СУНЦ МГУ <auto@automail.aesc.msu.ru>', [up.user.email, up.answer_profile.filter(question=add_email)[0].answer])
                #msg.content_subtype = "html"
                else:
                    msg = mail.EmailMessage(ext.letter_abs, ext.letter + '\n--\n\nThis letter is generated automatically. Responses are not processed.', 'Личный Кабинет СУНЦ МГУ <auto@automail.aesc.msu.ru>', [up.user.email,])
                try:
                    connection.send_messages([msg,])
                except Exception:        
                    data[i].append("cannot send email")                
                else:
                    data[i].append("email sent")
        else:
            data[i].append(user_identify(data[i][0], data[i][1], data[i][2], data[i][3]))
    if label == 'find':
        data[0] = data[0] + ['res ' + str(timezone.now()), 'Surname', 'Name', 'ParentName', 'BirthDay', 'E-mail']
    elif er == '':
        data[0].append('res ' + str(timezone.now()) + '\nno errors')
    else:
        data[0].append('res ' + str(timezone.now()) + er)    
    f = open('/var/www/lk/media/external/' + str(filename), 'wb')
    wrtr = csv.writer(f, delimiter=';')
    if ext.is_utf:
        for d in data:
            wrtr.writerow(d)  
    else:
        for d in code_to_newcode(data, 'utf8', 'cp1251'):
            wrtr.writerow(d)      

def send_all(filename):
    ext = External.objects.get(id=filename[:filename.find('_')])
    data = []
    ups = UserProfile.objects.filter(user__is_active=True)
    for up in ups:
        connection = mail.get_connection()
        msg = mail.EmailMessage(ext.letter_abs, ext.letter + '\n--\n\nThis letter is generated automatically. Responses are not processed.', 'Личный Кабинет СУНЦ МГУ <auto@automail.aesc.msu.ru>', [up.user.email,])
        row=[up.user.email, up.sname.encode('utf8'), up.name.encode('utf8'), up.pname.encode('utf8'), up.bday]
        try:
            connection.send_messages([msg,])
        except Exception:        
            row.append("cannot send email")                
        else:
            row.append("email sent") 
        data.append(row) 
    f = open('/var/www/lk/media/send_all/' + filename, 'wb')
    wrtr = csv.writer(f, delimiter=';')   
    for d in data:
        wrtr.writerow(d)   


def make_result(filename):
    form = Form.objects.get(id=filename[:filename.find('_')])
    f = open('/var/www/lk/media/result/{}'.format(filename), 'r')
    data = code_to_newcode([row for row in csv.reader(f, delimiter=';')], 'cp1251', 'utf8')
    data[0].append('res ' + str(timezone.now()))
    for i in range(1,len(data)):
        if user_identify(data[i][0], data[i][1], data[i][2], data[i][3]) != 'ok':
            data[i].append(user_identify(data[i][0], data[i][1], data[i][2], data[i][3]))
        else:
            u = UserProfile.objects.filter(sname=data[i][0], name=data[i][1], pname=data[i][2], bday=data[i][3])[0]
            rr = RegRes.objects.filter(user = u, form=form, is_checkin=True)
            if rr:
                rr[0].short_result, rr[0].detail_result, rr[0].private_result = 0, '', ''
                if data[i][4] == 'yes':
                    rr[0].short_result, rr[0].detail_result = 1, data[0][4]
                elif data[i][5] == 'yes':
                    rr[0].short_result, rr[0].detail_result = 3, data[0][5]
                elif data[i][6] == 'yes':
                    rr[0].short_result, rr[0].detail_result = 2, data[0][6]
                for j in range(7, len(data[0])):
                    if data[0][j][:3].lower() == 'pdf':
                        pass
                    elif data[0][j][:3].lower() == 'res' or data[0][j][:3].lower() == 'dip':
                        break
                    elif data[0][j][:4].lower() == 'priv':
                        rr[0].private_result = rr[0].private_result + '</br>{}: {}'.format(data[0][j][5:], data[i][j])
                    else:
                        rr[0].detail_result = rr[0].detail_result + '</br>{}: {}'.format(data[0][j], data[i][j])
                rr[0].save()
                data[i].append('ok')
            else:
                data[i].append('not checked in')
    form.last_res_publication = timezone.now()
    form.save()
    f = open('/var/www/lk/media/result/{}'.format(filename), 'wb')
    wrtr = csv.writer(f, delimiter=';')
    for d in code_to_newcode(data, 'utf8', 'cp1251'):
        wrtr.writerow(d)


def make_diplom(filename):
    form = Form.objects.get(id=filename[:filename.find('_')])
    f = open('/var/www/lk/media/result/{}'.format(filename), 'r')
    data = code_to_newcode([row for row in csv.reader(f, delimiter=';')], 'cp1251', 'utf8')
    data[0].append('dip ' + str(timezone.now()))
    for i in range(1,len(data)):
        if user_identify(data[i][0], data[i][1], data[i][2], data[i][3]) != 'ok':
            data[i].append(user_identify(data[i][0], data[i][1], data[i][2], data[i][3]))
        else:
            u = UserProfile.objects.filter(sname=data[i][0], name=data[i][1], pname=data[i][2], bday=data[i][3])[0]
            if u.year == 0 or u.year == 1900 or u.year == 2100:
                data[i].append('illegal user')
            else:
                cdo = []
                for j in range(7, len(data[0])):
                    if data[0][j][:3].lower() == 'pdf':
                        if form.id in all_io and data[i][j] == 'yes':
                            diplom(u.user.id, data[0][j], '2019')
                            u.diploms = u.diploms + '</br>2019: <a href="/lk/forms/download/pdf/{}_2019">{}</a>'.format(data[0][j][4:data[0][j].find(' ')],
                                                                                                                        data[0][j][4:data[0][j].find(' ')-1])
                        elif (form.id in all_cdo) and data[i][j] == 'yes':  # all cdo certificates
                            cdo.append(data[0][j][4:])
                    elif data[0][j][:3].lower() == 'res' or data[0][j][:3].lower() == 'dip':
                        break
                if len(cdo) in range(1, 3):    # certificate disk (less then 3 subjects)
                    disk(u.user.id, 'по ' + ', '.join(cdo), '2019')
                    u.diploms = u.diploms + '</br>2019: <a href="/lk/forms/download/pdf/certificate_disk_2019">DisC</a>'
                elif len(cdo) > 2:
                    certificate(u.user.id,  'по ' + ', '.join(cdo), '2019')
                    u.diploms = u.diploms + '</br>2019: <a href="/lk/forms/download/pdf/certificate_zash_2019">Zash</a>'
                u.save()
                data[i].append('diploms made')
    f = open('/var/www/lk/media/result/{}'.format(filename), 'wb')
    wrtr = csv.writer(f, delimiter=';')
    for d in code_to_newcode(data, 'utf8', 'cp1251'):
        wrtr.writerow(d)

 
def compare_lists(filename):
    form = Form.objects.get(id=filename[:filename.find('_')])
    f = open('/var/www/lk/media/default/' + filename, 'r')
    data = code_to_newcode([row for row in csv.reader(f, delimiter=';')], 'cp1251', 'utf8')
    l = len(data[0])
    data[0] = data[0] + ['res ' + str(timezone.now()), 'Surname', 'Name', 'ParentName', 'BirthDay', 'E-mail']
    for i in range(1,len(data)):
        ar = ya_user_identify(data[i][0], data[i][1], data[i][2], data[i][3])
        if ar:
            if ar[0] == 'ok':
                if not RegRes.objects.filter(user=UserProfile.objects.filter(sname=data[i][0], name=data[i][1], pname=data[i][2], bday=data[i][3])[0], form=form, is_checkin=True):
                    ar[0] = 'not checked in'
            data[i] = data[i] + ar
    for rr in RegRes.objects.filter(form=form, is_checkin=True):
        fl = False
        for i in range(1,len(data)):
            if rr.user.sname.encode('utf8').lower() == data[i][0].lower() and rr.user.name.encode('utf8').lower() == data[i][1].lower() and rr.user.pname.encode('utf8').lower() == data[i][2].lower() and str(rr.user.bday).lower() == data[i][3].lower():
                fl = True
        if not fl:                
            s = ['non legal', rr.user.sname.encode('utf8'), rr.user.name.encode('utf8'), rr.user.pname.encode('utf8'), str(rr.user.bday), rr.user.user.email.encode('utf8')]
            fll = False
            for i in range(1,len(data)):
                if len(data[i]) == l and not fll:
                    data[i] = data[i] + s
                    fll = True
            if not fll:
                data.append(['' for i in range(1, l+1)] + s)
    f = open('/var/www/lk/media/default/' + filename, 'wb')
    wrtr = csv.writer(f, delimiter=';')
    for d in code_to_newcode(data, 'utf8', 'cp1251'):
        wrtr.writerow(d)

def check_test(filename):
    form = Form.objects.get(id=filename[:filename.find('_')])
    f = open('/var/www/lk/media/answers/' + filename, 'r')
    data = [row for row in csv.reader(f, delimiter=';')]
    if len(data) > 5:      
        for i in range(5,len(data)):
            data.pop()
    all = 0
    for i in range(4,len(data[0])):
        all = all + int(data[4][i])
    if len(data[1]) == len(data[0]):  
        data[1] = data[1] + ['points (' + str(all) + ')', '% (100)', '']
        add = True
    else:
        add = False
    err = []
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
        for rr in RegRes.objects.filter(form=form, is_checkin=True).order_by('user__sname'): 
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
                        ss.append('['+str(data[4][i])+']')
                        sum = sum + int(data[4][i])
                        add_ss.append(user_ans)
                    else:
                        ss.append(user_ans + ' ' )
                        add_ss.append('')
            ss = ss + [sum, round(float(sum)/float(all)*100.0), '']
            data.append(ss+add_ss)
        data.append(['no errors'])
            
    data.append(['was checked',timezone.now().strftime("%Y-%m-%d %H:%M")])
    f = open('/var/www/lk/media/answers/' + filename, 'wb')
    wrtr = csv.writer(f, delimiter=';')
    for d in data:
        wrtr.writerow(d)
        
def do_reg_to_archive(form_id):
    f = Form.objects.get(id=form_id)
    for rr in f.regres_list.all():
        if rr.is_checkin:
            rr.is_checkin = False
            if rr.short_result == 0 and rr.detail_result == '' and rr.private_result == '':
                rr.delete()
            else:
                rr.save()
            if ArchiveRegRes.objects.filter(form=rr.form).filter(user=rr.user):
                arr = ArchiveRegRes.objects.filter(form=rr.form).filter(user=rr.user)[0]
                arr.is_checkin = True
                arr.save()
            else:
                arr = ArchiveRegRes.objects.create(user=rr.user, form=rr.form, form_name=rr.form.name, is_checkin=True)
                arr.save()
    f.last_reg_archivation = timezone.now()
    f.save()


def do_res_to_archive(form_id):
    f = Form.objects.get(id=form_id)
    for rr in f.regres_list.all():
        if rr.short_result != 0 or rr.detail_result != '' or rr.private_result != '':
            if ArchiveRegRes.objects.filter(form=rr.form).filter(user=rr.user):
                arr = ArchiveRegRes.objects.filter(form=rr.form).filter(user=rr.user)[0]
                arr.short_result = rr.short_result
                arr.detail_result = rr.detail_result
                arr.private_result = rr.private_result
                arr.save()
            else:
                arr = ArchiveRegRes.objects.create(user=rr.user, form=rr.form, form_name=rr.form.name, short_result=rr.short_result, detail_result=rr.detail_result, private_result=rr.private_result)
                arr.save()
            if rr.is_checkin:
                rr.short_result = 0
                rr.detail_result = ''
                rr.private_result = ''
                rr.save()
            else:
                rr.delete()
    f.last_res_archivation = timezone.now()
    f.save()   


def do_qn_to_archive(q_id):
    q = Question.objects.get(id=q_id)
    for a in q.answer_list.all():
        aa = ArchiveAnswer.objects.create(user=a.user, question_text=a.question.name, answer=a.answer)
        aa.save()
        a.delete()    


def reg_to_archive(req, form_id):
    do_reg_to_archive(form_id)  
    return HttpResponseRedirect(back(req)) 

def res_to_archive(req, form_id):
    do_res_to_archive(form_id)  
    return HttpResponseRedirect(back(req))  

def qn_to_archive(req, q_id):
    do_qn_to_archive(q_id)    
    return HttpResponseRedirect(back(req))
    
@user_passes_test(activation_check)	
def showform(req, form_id):
    f = Form.objects.get(id=form_id)
    up = req.user.profile.all()[0]
    if req.user.is_superuser or req.user.groups.filter(Q(id=1) | Q(id=4) | Q(id=5)) or req.user == f.owner or req.user in f.editor.all() or req.user in f.reader.all() or req.user in f.just_user.all() or RegRes.objects.filter(user=up, form=f, is_checkin=True):
        return render(req, 'lkforms/form.html',{'form': f, 'qns': [fq.question for fq in f.fmqn_fmlist.order_by('number')], 'just_show': 'just_show', 'back': back(req)})  
    return HttpResponseRedirect(back(req))

        
@user_passes_test(administrator_check)   
def new_external(req):
    External.objects.create(original='Новый объект ' + timezone.now().strftime("%Y-%m-%d %H:%M:%S"), owner = req.user)
    return HttpResponseRedirect(back(req))

def delete_email(req, user_id):
    f = open('/var/www/lk/media/txt/log.txt', 'wb')
    txt = ''
    connection = mail.get_connection()
    user = User.objects.get(id=user_id)
    ext = External.objects.get(id=112)
    msg = mail.EmailMessage(ext.letter_abs, ext.letter + '\n--\n\nThis letter is generated automatically. Responses are not processed.', 'Личный Кабинет СУНЦ МГУ <auto@automail.aesc.msu.ru>', [user.email,] )
    try:
        connection.send_messages([msg,])
    except Exception:        
        txt =  txt + "cannot send email"                
    else:
        txt = txt + "email sent"
    f.writelines(txt)
    f = open('/var/www/lk/media/txt/log.txt', 'rb')
    return HttpResponse(f, content_type='application/octet-stream')  
    
def diplom(user_id, s, year): 
    u = User.objects.get(id=user_id).profile.all()[0]
    if u.year == int(year) + 1:
        cl = '10'
    elif u.year == int(year) + 2:
        cl = '9'
    elif u.year == int(year) + 3:
        cl = '8'
    elif u.year >= int(year) + 4:
        cl = '7'
    f = open('/var/www/lk/media/pdf/' + str(user_id) + '_' + s.split()[0][4:] + '_' + year + '.pdf', 'w')
    p = canvas.Canvas('/var/www/lk/media/pdf/' + str(user_id) + '_' + s.split()[0][4:] + '_' + year + '.pdf')
    w, h = A4
    pdfmetrics.registerFont(TTFont('BookAntiqua', '/var/www/lk/media/media/myfonts/BookAntiqua.ttf'))
    pdfmetrics.registerFont(TTFont('TimesNewRoman', '/var/www/lk/media/media/myfonts/TimesNewRoman.ttf'))
    pdfmetrics.registerFont(TTFont('MonotypeCorsiva', '/var/www/lk/media/media/myfonts/MonotypeCorsiva.ttf'))
    p.drawImage('/var/www/lk/media/media/diplom' + year + '.jpg', 0, 0, width=w, height=h)
    p.setFont('BookAntiqua', 56)
    p.drawCentredString(w/2, h/2 + 120, 'Диплом')
    p.setFont('TimesNewRoman', 18)
    p.drawCentredString(w/2, h/2 + 65, s.split()[2])
    p.drawCentredString(w/2, h/2 + 45, 'интернет-олимпиады СУНЦ МГУ')
    p.drawCentredString(w/2, h/2 + 25, s.split()[3] + ' ' + s.split()[4])
    p.drawCentredString(w/2, h/2 + 5, 'среди учащихся ' + cl + ' класса')
    p.drawCentredString(w/2, h/2 - 55, 'награждается')
    if (len(u.sname) + len(u.name) + len(u.pname)) < 25:
        p.setFont('MonotypeCorsiva', 38)
    elif (len(u.sname) + len(u.name) + len(u.pname)) < 28:
        p.setFont('MonotypeCorsiva', 36)
    else:
        p.setFont('MonotypeCorsiva', 32)
    p.drawCentredString(w/2, h/2 - 110, u.sname + ' ' + u.name + ' ' + u.pname)
 #   p.setFont('MonotypeCorsiva', 26)
 #   p.drawCentredString(w/2, h/2 - 145, 'дата рождения ' + str(u.bday))
    p.showPage()
    p.save() 
    
def certificate(user_id, s, year): 
    u = User.objects.get(id=user_id).profile.all()[0]
    if u.year == int(year) + 1:
        cl = '10'
    elif u.year == int(year) + 2:
        cl = '9'
    elif u.year == int(year) + 3:
        cl = '8'
    elif u.year == int(year) + 4:
        cl = '7'
    f = open('/var/www/lk/media/pdf/' + str(user_id) + '_certificate_zash_' + year + '.pdf', 'w')
    p = canvas.Canvas('/var/www/lk/media/pdf/' + str(user_id) + '_certificate_zash_' + year + '.pdf')
    w, h = A4
    pdfmetrics.registerFont(TTFont('TimesNewRoman', '/var/www/lk/media/media/myfonts/TimesNewRoman.ttf'))
    pdfmetrics.registerFont(TTFont('MonotypeCorsiva', '/var/www/lk/media/media/myfonts/MonotypeCorsiva.ttf'))
    p.drawImage('/var/www/lk/media/media/certificate_zash_' + year + '.jpg', 0, 0, width=w, height=h)
    p.setFont('TimesNewRoman', 17)
    p.drawCentredString(w/2, h/2 + 55, 'об окончании ' + cl + ' класса Заочной школы СУНЦ МГУ')
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
    p.drawCentredString(w/2, 344, cl + ' класса ЗШ СУНЦ МГУ')
    p.drawCentredString(w/2, 323, s)
    p.showPage()
    p.save()
    
    
def disk(user_id, s, year): 
    u = User.objects.get(id=user_id).profile.all()[0]
    if u.year == int(year) + 1:
        cl = '10'
    elif u.year == int(year) + 2:
        cl = '9'
    elif u.year == int(year) + 3:
        cl = '8'
    elif u.year == int(year) + 4:
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

def get_ans(form, user):    # ответы из формы form в виде списка (for 'generate_mm')
    line = []
    for fmqn in form.fmqn_fmlist.order_by('number'):
        if Answer.objects.filter(user=user, question=fmqn.question):
            line.append( Answer.objects.filter(user=user, question=fmqn.question)[0].answer.encode('utf-8') )
        else:
            line.append( '---' )
    return line
        
def generate_mm(req):
    f = open('/var/www/lk/media/data/mm.csv', 'wb')
    m0 = Form.objects.get(id=163)  # заявка команды
    m_accomp = Form.objects.get(id=164)  # данные о сопровождающем
    m_main = [ Form.objects.get(id=i) for i in [165,169,170,171] ]  # данные об участниках 1-4
    m_confirm = Form.objects.get(id=166)  # подтверждение приезда
    data = []
    first = ( [ str(qn.number)+'.'+qn.question.name.encode('utf-8') for qn in m_main[0].fmqn_fmlist.order_by('number') ] +
              [ str(qn.number)+'.'+qn.question.name.encode('utf-8') for qn in m_accomp.fmqn_fmlist.order_by('number') ] +
              [ str(qn.number)+'.'+qn.question.name.encode('utf-8') for qn in m0.fmqn_fmlist.order_by('number')] +
              [ str(qn.number)+'.'+qn.question.name.encode('utf-8') for qn in m_confirm.fmqn_fmlist.order_by('number')] )
    data.append(first)
    for rr in m0.regres_list.all():
        for m in m_main:
            if m.regres_list.filter(user=rr.user):
                data.append( get_ans(m, rr.user) + get_ans(m_accomp, rr.user) + get_ans(m0, rr.user) + get_ans(m_confirm, rr.user) )   
    wrtr = csv.writer(f, delimiter=';')
    for d in data:
        wrtr.writerow(d)
    f = open('/var/www/lk/media/data/mm.csv', 'rb')
    return HttpResponseRedirect(back(req))

def anketa(user_id, form_id): 
    u = User.objects.get(id=user_id).profile.all()[0]
    f = open('/var/www/lk/media/pdf/' + str(user_id) + '_anketa.pdf', 'w')
    p = canvas.Canvas('/var/www/lk/media/pdf/' + str(user_id) + '_anketa.pdf')
    w, h = A4
    pdfmetrics.registerFont(TTFont('TimesNewRoman', '/var/www/lk/media/media/myfonts/TimesNewRoman.ttf'))
    p.drawImage('/var/www/lk/media/media/anketa.jpg', 0, 0, width=w, height=h)
    p.setFont('TimesNewRoman', 9)
    if u.regres_profile.filter(form=Form.objects.get(id=160)):  # 9 class
        p.drawString(113, 721, 'X')
        p.drawString(525, 426, '9')
    elif u.regres_profile.filter(form=Form.objects.get(id=159)):    # 10 class
        p.drawString(226, 721, 'X')
        p.drawString(525, 426, '10')
    if form_id=='289' or form_id=='296':            # 10-pm                
        p.drawString(113, 687, 'X') 
    elif form_id=='288' or form_id=='294':        # 10-cb
      #  if u.answer_profile.filter(question=Question.objects.get(id=104)):  # missing qn
       #     if str(u.answer_profile.filter(question=Question.objects.get(id=104))[0].answer.encode('utf8')) == '10хим':
       #         p.drawString(113, 679, 'X')
       #     elif str(u.answer_profile.filter(question=Question.objects.get(id=104))[0].answer.encode('utf8')) == '10био':
       #         p.drawString(228, 679, 'X')
        #    elif str(u.answer_profile.filter(question=Question.objects.get(id=104))[0].answer.encode('utf8')) == '10хб':
        p.drawString(342, 679, 'X')
    if form_id=='294' or form_id=='295' or form_id=='296':  # Moscow exams
        p.drawString(245, 662, 'Москва')
    elif form_id=='290':         # place of exam - 11-pm
        if u.answer_profile.filter(question=Question.objects.get(id=16)):         
            p.drawString(245, 662, u.answer_profile.filter(question=Question.objects.get(id=16))[0].answer)   
    elif form_id=='289':         # place of exam - 10-pm
        if u.answer_profile.filter(question=Question.objects.get(id=112)):         
            p.drawString(245, 662, u.answer_profile.filter(question=Question.objects.get(id=112))[0].answer)
    elif form_id=='288':          # place of exam - 10-cb
        if u.answer_profile.filter(question=Question.objects.get(id=19)):         
            p.drawString(245, 662, u.answer_profile.filter(question=Question.objects.get(id=19))[0].answer)            
    p.drawString(113, 623, 'X')            
    p.drawString(100, 588, u.sname)       
    p.drawString(380, 588, u.name)      
    p.drawString(100, 570, u.pname)      
    p.drawString(360, 553, u.bday.strftime("%d.%m.%Y"))     
    if u.sex == 1:                    
        p.drawString(211, 535, 'ж')
    elif u.sex == 2:
        p.drawString(211, 535, 'м')
    if u.answer_profile.filter(question=Question.objects.get(id=21)):      
        p.drawString(360, 535, u.answer_profile.filter(question=Question.objects.get(id=21))[0].answer)
    if u.answer_profile.filter(question=Question.objects.get(id=22)):       
        p.drawString(330, 517, u.answer_profile.filter(question=Question.objects.get(id=22))[0].answer)
    if u.answer_profile.filter(question=Question.objects.get(id=23)):       
        p.drawString(360, 499, u.answer_profile.filter(question=Question.objects.get(id=23))[0].answer)
    if u.answer_profile.filter(question=Question.objects.get(id=92)):       
        p.drawString(280, 480, u.answer_profile.filter(question=Question.objects.get(id=92))[0].answer)
    if u.answer_profile.filter(question=Question.objects.get(id=26)):     
        p.drawString(211, 462, u.answer_profile.filter(question=Question.objects.get(id=26))[0].answer)
    if u.answer_profile.filter(question=Question.objects.get(id=93)):      
        p.drawString(360, 444, u.answer_profile.filter(question=Question.objects.get(id=93))[0].answer)
    if u.answer_profile.filter(question=Question.objects.get(id=28)):    
        p.drawString(135, 426, u.answer_profile.filter(question=Question.objects.get(id=28))[0].answer)
        # 17 go to 1
    if u.answer_profile.filter(question=Question.objects.get(id=29)):      
        p.drawString(135, 408, u.answer_profile.filter(question=Question.objects.get(id=29))[0].answer)
    p.drawString(115, 390, u.user.email)                      
    if u.answer_profile.filter(question=Question.objects.get(id=31)):         
        p.drawString(135, 372, u.answer_profile.filter(question=Question.objects.get(id=31))[0].answer)
    if u.answer_profile.filter(question=Question.objects.get(id=30)):       
        p.drawString(115, 355, u.answer_profile.filter(question=Question.objects.get(id=30))[0].answer)
    if u.answer_profile.filter(question=Question.objects.get(id=179)):      
        if str(u.answer_profile.filter(question=Question.objects.get(id=179))[0].answer.encode('utf8')) == 'да':
            p.drawString(81, 325, 'X')
        elif str(u.answer_profile.filter(question=Question.objects.get(id=179))[0].answer.encode('utf8')) == 'очень хочу':
            p.drawString(81, 315, 'X')
        elif str(u.answer_profile.filter(question=Question.objects.get(id=179))[0].answer.encode('utf8')) == 'хочу':
            p.drawString(309, 325, 'X')
        elif str(u.answer_profile.filter(question=Question.objects.get(id=179))[0].answer.encode('utf8')) == 'нет':
            p.drawString(309, 315, 'X')
    if u.answer_profile.filter(question=Question.objects.get(id=422)):         
        if str(u.answer_profile.filter(question=Question.objects.get(id=422))[0].answer.encode('utf8')) == 'Нуждаюсь':
            p.drawString(81, 286, 'X')
        elif str(u.answer_profile.filter(question=Question.objects.get(id=422))[0].answer.encode('utf8')) == 'Нуждаюсь, но могу обойтись':
            p.drawString(179, 286, 'X')
        elif str(u.answer_profile.filter(question=Question.objects.get(id=422))[0].answer.encode('utf8')) == 'Не нуждаюсь':
            p.drawString(309, 286, 'X')
    if u.answer_profile.filter(question=Question.objects.get(id=435)):         # passport
        if str(u.answer_profile.filter(question=Question.objects.get(id=435))[0].answer.encode('utf8')) == 'Да':
            if u.answer_profile.filter(question=Question.objects.get(id=68)): 
                p.drawString(95, 200, u.answer_profile.filter(question=Question.objects.get(id=68))[0].answer)
            if u.answer_profile.filter(question=Question.objects.get(id=69)): 
                p.drawString(425, 200, u.answer_profile.filter(question=Question.objects.get(id=69))[0].answer)  
            if u.answer_profile.filter(question=Question.objects.get(id=70)): 
                p.drawString(105, 182, u.answer_profile.filter(question=Question.objects.get(id=70))[0].answer)  
        elif str(u.answer_profile.filter(question=Question.objects.get(id=435))[0].answer.encode('utf8')) == 'Нет':     # no passport
            if u.answer_profile.filter(question=Question.objects.get(id=68)): 
                p.drawString(470, 152, u.answer_profile.filter(question=Question.objects.get(id=68))[0].answer)
            if u.answer_profile.filter(question=Question.objects.get(id=69)) and u.answer_profile.filter(question=Question.objects.get(id=70)): 
                p.drawString(35, 134, u.answer_profile.filter(question=Question.objects.get(id=69))[0].answer + ' ' + u.answer_profile.filter(question=Question.objects.get(id=70))[0].answer)          
    p.showPage()
    p.save()
    
