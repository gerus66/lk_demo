from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils import timezone
from lkmoderation.models import MForm, Request, MFmQn, MFmMQn, MQuestion, QRequest
from lkforms.models import Form, FmQn, Question, Variant, Theme
from django.contrib.auth.models import Group, User
from django.contrib.auth.decorators import user_passes_test
from lkforms.views import do_reg_to_archive, do_res_to_archive, do_qn_to_archive
from django.core import mail
  
def administrator_check(user):
    return Group.objects.get(id=2) in user.groups.all()
    
def moderator_check(user):
    return Group.objects.get(id=1) in user.groups.all()
    
def superuser_check(user):
    return user.is_superuser

@user_passes_test(moderator_check)    
def index(req):
    return render(req, 'lkmoderation/app_index.html', {'form_mod_count': str(Request.objects.filter(passed=0).count()), 'qn_mod_count': str(QRequest.objects.filter(passed=0).count())})


def back(req):
    try: 
        req.META['HTTP_REFERER']
    except KeyError:
        return '/lk/'
    else:
        return req.META['HTTP_REFERER']  

        
@user_passes_test(administrator_check)   
def new_mform(req):
    MForm.objects.create(name='Новая форма ' + timezone.now().strftime("%Y-%m-%d %H:%M:%S"), full_name='Новая форма ' + timezone.now().strftime("%Y-%m-%d %H:%M:%S"), theme = Theme.objects.get(id=1), owner = req.user)
    return HttpResponseRedirect(back(req))
    
@user_passes_test(administrator_check)   
def new_mquestion(req):
    MQuestion.objects.create(name='Новый вопрос ' + timezone.now().strftime("%Y-%m-%d %H:%M:%S"), owner = req.user)
    return HttpResponseRedirect(back(req))
        
@user_passes_test(superuser_check)   
def new_syn_mform(req, f_id):
    f = Form.objects.get(id=f_id)
    mf = MForm.objects.create(name=f.name, full_name=f.full_name, theme=f.theme, info=f.info, clarification=f.clarification, syn_form=f, owner = f.owner, mod_pass=2)
    mf.editor = f.editor.all()
    mf.reader = f.reader.all()
    mf.save()
    for fq in f.fmqn_fmlist.all():
        MFmQn.objects.create(form=mf, question=fq.question, number=fq.number)
    moders = [u for u in User.objects.all() if moderator_check(u)]
    Request.objects.create(form=mf, author=mf.owner, type=1, moderator=moders[0], passed=1)
    return HttpResponseRedirect(back(req))

    
@user_passes_test(administrator_check)     
def sfdelete(req, form_id):
    mf = MForm.objects.get(id=form_id)
    if req.user == mf.owner and mf.mod_pass <> 1 and not mf.syn_form:
        if Request.objects.filter(form=mf):
            Request.objects.filter(form=mf)[0].delete()
        for mqf in mf.mfmqn_fmlist.all():
            mqf.delete()
        for mqf in mf.mfmmqn_fmlist.all():
            mqf.delete()
        mf.delete()
    return HttpResponseRedirect(back(req))   
    
@user_passes_test(administrator_check)     
def sqdelete(req, qn_id):
    mq = MQuestion.objects.get(id=qn_id)
    if req.user == mq.owner:
        for mqf in mq.mfmmqn_qnlist.all():
            mqf.delete()
        mq.delete()
    return HttpResponseRedirect(back(req))
    
@user_passes_test(administrator_check)     
def askmod(req, sub_id, type):
    fl = True
    if int(type) < 10:
        mf = MForm.objects.get(id=sub_id)
        if (req.user == mf.owner or req.user in mf.editor.all()) and mf.mod_pass <> 1:
            if Request.objects.filter(form=mf):
                r = Request.objects.filter(form=mf)[0]
                r.passed = 0
                r.type = int(type)
                r.save()
            else:
                Request.objects.create(form=mf, author=req.user, type=int(type))
            mf.mod_pass = 1
            mf.save()
            connection = mail.get_connection()
            msg = mail.EmailMessage('Поступил запрос на модерацию в Личном кабинете СУНЦ МГУ', '<a href="http://lk.internat.msu.ru/lk/mod/modform/">Form moderation</a><br>--<br><br>This letter is generated automatically. Responses are not processed.', 'Личный Кабинет СУНЦ МГУ <auto@automail.aesc.msu.ru>', ['andrej2501@yandex.ru',])
            msg.content_subtype = "html"
            try:
                connection.send_messages([msg,])
            except Exception:           
                fl = False
            else:
                fl = True
    else:
        qn_type = str(type)[1]
        qn = Question.objects.get(id=sub_id)
        if QRequest.objects.filter(question=qn):
            qr = QRequest.objects.filter(question=qn)[0]
            qr.passed = 0
            qr.type = int(qn_type)
            qr.save()
        else:
            QRequest.objects.create(question=qn, author=req.user, type=int(qn_type))
        connection = mail.get_connection()
        msg = mail.EmailMessage('Поступил запрос на модерацию в Личном кабинете СУНЦ МГУ', '<a href="http://internat2014.ru/lk/mod/modqn/">Question moderation</a><br>--<br><br>This letter is generated automatically. Responses are not processed.', 'Личный Кабинет СУНЦ МГУ <auto@automail.aesc.msu.ru>', ['andrej2501@yandex.ru',])
        msg.content_subtype = "html"
        try:
            connection.send_messages([msg,])
        except Exception:           
            fl = False
        else:
            fl = True
    return HttpResponseRedirect(back(req))

       
def showform(req, form_id):
    f = MForm.objects.get(id=form_id)
    if req.user.is_superuser or req.user.groups.filter(id=1) or req.user == f.owner or req.user in f.editor.all():
        return render(req, 'lkforms/form.html',{'form': f, 'qns': [fq.question for fq in f.mfmqn_fmlist.order_by('number')] + [qn.question for qn in f.mfmmqn_fmlist.order_by('number')], 'just_show': 'just_show', 'back': back(req)})  
    return HttpResponseRedirect(back(req))

    
@user_passes_test(moderator_check)
def modform(req):
    if req.POST:
        for r in Request.objects.all():
            if req.POST.get(str(r.id) + '_comms', ''):
                r.form.comms = r.form.comms + timezone.now().strftime("%Y-%m-%d %H:%M:%S") + ': ' + req.POST.get(str(r.id) + '_comms', '') + '<br>'
                r.form.save()
            if req.POST.get(str(r.id) + '_passed', ''):
                r.moderator = req.user
                if req.POST.get(str(r.id) + '_passed', '') == 'yes':
                    r.passed = 1
                    r.form.mod_pass = 2
                    r.save()
                    r.form.save()
                    if r.type == 0:      
                        for qf in r.form.syn_form.fmqn_fmlist.all():
                            qf.delete()
                        r.form.syn_form.delete()
                        for mqf in r.form.mfmqn_fmlist.all():
                            mqf.delete()
                        for mqf in r.form.mfmmqn_fmlist.all():
                            mqf.delete()
                        r.form.delete()
                        r.delete()
                    elif r.type == 1:     
                        f = Form.objects.create(full_name=r.form.full_name, name=r.form.name, theme=r.form.theme, user_theme = Theme.objects.get(id=1), info=r.form.info, owner=r.form.owner)
                        for mqf in r.form.mfmqn_fmlist.all():
                            FmQn.objects.create(form=f, question=mqf.question, number=mqf.number)
                        for mqf in r.form.mfmmqn_fmlist.all():
                            q = Question.objects.create(name=mqf.question.name, comms=mqf.question.comms, not_blank=mqf.question.not_blank, with_vars=mqf.question.with_vars, multi_vars=mqf.question.multi_vars)
                            for v in mqf.question.variant_list.all():
                                Variant.objects.create(question=q, name=v.name)
                                v.delete()
                            FmQn.objects.create(form=f, question=q, number=mqf.number)
                            MFmQn.objects.create(form=r.form, question=q, number=mqf.number)
                            mqf.question.delete()
                            mqf.delete()
                        r.form.syn_form = f
                        r.form.save()
                        for read in r.form.reader.all():
                            read.is_staff = True
                            read.groups.add(Group.objects.get(id=3))
                            read.save()
                        r.form.syn_form.reader = r.form.reader.all()
                        r.form.syn_form.editor = r.form.editor.all()
                        r.form.syn_form.save()
                    elif r.type == 2:  
                        for qf in r.form.syn_form.fmqn_fmlist.all():
                            qf.delete()
                        for mqf in r.form.mfmqn_fmlist.all():
                            FmQn.objects.create(form=r.form.syn_form, question=mqf.question, number=mqf.number)
                        for mqf in r.form.mfmmqn_fmlist.all():
                            q = Question.objects.create(name=mqf.question.name, comms=mqf.question.comms, not_blank=mqf.question.not_blank, with_vars=mqf.question.with_vars, multi_vars=mqf.question.multi_vars)
                            for v in mqf.question.variant_list.all():
                                Variant.objects.create(question=q, name=v.name)
                                v.delete()
                            FmQn.objects.create(form=r.form.syn_form, question=q, number=mqf.number)
                            MFmQn.objects.create(form=r.form, question=q, number=mqf.number)
                            mqf.question.delete()
                            mqf.delete()
                        for read in r.form.reader.all():
                            read.is_staff = True
                            read.groups.add(Group.objects.get(id=3))
                            read.save()
                        r.form.syn_form.reader = r.form.reader.all()
                        r.form.syn_form.editor = r.form.editor.all()
                        r.form.syn_form.save()
                    elif r.type == 3:   
                        do_reg_to_archive(r.form.syn_form.id)
                    elif r.type == 4:    
                        do_res_to_archive(r.form.syn_form.id)
                elif req.POST.get(str(r.id) + '_passed', '') == 'no':
                    r.passed = 2
                    r.form.mod_pass = 3
                    r.save()
                    r.form.save()
    return render(req, 'lkmoderation/modform.html',{'mrs': Request.objects.order_by('-changed')})   
    
@user_passes_test(moderator_check)
def modqn(req):
    if req.POST:
        for r in QRequest.objects.all():           
            if req.POST.get(str(r.id) + '_comms', ''):
                r.comms = r.comms + timezone.now().strftime("%Y-%m-%d %H:%M:%S") + ': ' + req.POST.get(str(r.id) + '_comms', '') + '<br>'
                r.save()
            if req.POST.get(str(r.id) + '_passed', ''):
                r.moderator = req.user
                if req.POST.get(str(r.id) + '_passed', '') == 'yes':
                    r.passed = 1
                    r.save()
                    if r.type == 0:      
                        for qf in r.question.fmqn_qnlist.all():
                            qf.delete()
                        for mqf in r.question.mfmqn_qnlist.all():
                            mqf.delete()
                        r.question.delete()
                        r.delete()
                    elif r.type == 1:  
                        do_qn_to_archive(r.question.id)
                elif req.POST.get(str(r.id) + '_passed', '') == 'no':
                    r.passed = 2
                    r.save()
    return render(req, 'lkmoderation/modqn.html',{'mrs': QRequest.objects.order_by('-changed')})  
    
   
def readform(req):
    if Group.objects.get(id=5) in req.user.groups.all():
        return render(req, 'lkmoderation/readform.html', {'fms': Form.objects.all()})
    return render(req, 'lkmoderation/readform.html', {'fms': req.user.use_forms.all()})
    
