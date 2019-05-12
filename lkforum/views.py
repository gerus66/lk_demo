from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from lkforum.models import QnAns, Receiver, Topic

def activation_check(user):
    return user.is_active
    
def receiver_check(user):
    return user.receiver_profile.all() and  user.is_active

@user_passes_test(activation_check)    
def index(req):
    if req.user.receiver_profile.all():
        return render(req, 'lkforum/app_index.html', {'count': str(QnAns.objects.filter(receiver=req.user.receiver_profile.all()[0], answer='').count())})
    else:
        return render(req, 'lkforum/app_index.html')
 
def topics(req):
    return render(req, 'lkforum/topics.html', {'tps': Topic.objects.all().order_by('number', 'name')})
    
def topic(req, t_id):
    qns = QnAns.objects.filter(is_private=False).exclude(answer='').order_by('-created')
    if t_id == '0':      
        return render(req, 'lkforum/topic.html', {'qas': qns, 't': 'Все вопросы', 'fl': True})
    else:                  
        t = Topic.objects.get(id=t_id)
        return render(req, 'lkforum/topic.html', {'qas': qns.filter(topic=t), 't': t.name, 'fl': False})
  
@user_passes_test(activation_check)    
def my_qns(req):
    if req.POST:
        for qa in QnAns.objects.filter(author=req.user):
            if req.POST.get(str(qa.id), ''):
                qa.is_private = True
            else:
                qa.is_private = False
            qa.save()
        for qa in QnAns.objects.filter(author=req.user):
            if req.POST.get('delete_' + str(qa.id), ''):
                qa.delete()
    return render(req, 'lkforum/my_qns.html', {'qas': QnAns.objects.filter(author=req.user).order_by('-created')})

@user_passes_test(activation_check)    
def new_qn(req):
    if req.POST:           
        if req.POST.get('q', '') and req.POST.get('t', ''):
            if req.POST.get('priv', ''):
                qa = QnAns.objects.create(author=req.user, topic=Topic.objects.filter(name=req.POST.get('t', '')).all()[0], receiver=Topic.objects.filter(name=req.POST.get('t', '')).all()[0].default_receiver, question=req.POST.get('q', ''), is_private=True)
            else:
                qa = QnAns.objects.create(author=req.user, topic=Topic.objects.filter(name=req.POST.get('t', '')).all()[0], receiver=Topic.objects.filter(name=req.POST.get('t', '')).all()[0].default_receiver, question=req.POST.get('q', ''))
            return render(req, 'lkforum/new_qn.html', {'txt': qa.make_receiver_email(), 'ts': Topic.objects.all()})
        else:
            return render(req, 'lkforum/new_qn.html', {'txt': 'Вы  не заполнили один из обязательных пунктов', 'q': req.POST.get('q', ''), 'tp': req.POST.get('t', ''), 'priv': req.POST.get('priv', ''), 'ts': Topic.objects.all() })
    else:    
        return render(req, 'lkforum/new_qn.html', {'ts': Topic.objects.all()})

@user_passes_test(receiver_check)     
def answers(req):
    if req.POST:
        for qa in QnAns.objects.filter(receiver=req.user.receiver_profile.all()[0], answer=''):
            qa.topic = Topic.objects.filter(name=req.POST.get('t_' + str(qa.id), ''))[0]
            if qa.receiver.post.strip() != req.POST.get('rc_' + str(qa.id), '').split('|')[-1].strip() :
                qa.receiver = Receiver.objects.filter(post=req.POST.get('rc_' + str(qa.id), '').split('|')[-1].strip())[0] 
                qa.make_receiver_email()
            qa.save()
    return render(req, 'lkforum/answers.html', {'qas': QnAns.objects.filter(receiver=req.user.receiver_profile.all()[0]).order_by('-created'), 'ts': Topic.objects.all(), 'rcs': Receiver.objects.all()})   
    
@user_passes_test(receiver_check)      
def answer(req, qa_id):
    qa = QnAns.objects.get(id=qa_id)
    if qa.receiver.user == req.user:
        if req.POST:
            qa.answer = req.POST.get('a', '')
            if req.POST.get('priv', ''):
                qa.is_private = True
            qa.save()
            return render(req, 'lkforum/answer.html', {'qa': qa, 'txt': qa.make_author_email()})
        else:
            return render(req, 'lkforum/answer.html', {'qa': qa})
    else:
        return render(req, '500.html')
