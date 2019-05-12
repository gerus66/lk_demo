from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.core import mail
from django.utils import timezone

from lkforms.models import Form
from lktest.inactives import delete_inactive
from lktest.nonvalids import delete_nonvalid
from lktest.noactions import delete_noaction
from lktest.forumonly import send_mails_forumonly, check_file_forumonly, delete_forumonly
from lktest.remind import make_remind_list, send_remind_list

def me_check(user):
    return user.id == 1
 
@user_passes_test(me_check) 
def email_ping(req):        
    connection = mail.get_connection()
    msg = mail.EmailMessage('lktest', 'ping!', 'Личный Кабинет СУНЦ МГУ <auto@automail.aesc.msu.ru>', ['unforgiven8@yandex.ru',])
    msg.content_subtype = "html"
    try:
        connection.send_messages([msg,])
    except Exception:           
        return render(req, 'lktest/app_index.html', {'ping': 'exception:(',})
    else:
        return render(req, 'lktest/app_index.html', {'ping': 'Ok:)',})

@user_passes_test(me_check) 
def all_forms(req): 
    thms = []
    for i in [1,20,14, 16, 17,18,21,22]:
        thms.append(Form.objects.filter(is_active=True, user_theme__id=i))
    return render(req, 'lktest/forms.html', {'thms': thms})
    


@user_passes_test(me_check)       
def some_page(req):
  #  form = Form.objects.get(id='70')
    return render(req, 'lktest/test_page.html')

@user_passes_test(me_check)
def inactive(req):
    txt = ''
    txt = delete_inactive()
    f = open('/var/www/lk/logs/inactive.log', 'wb')
    f.writelines(txt)
    return render(req, 'lktest/log.html', {'txt': txt})

@user_passes_test(me_check)
def nonvalid(req):
    txt = ''
    txt = delete_nonvalid()
    f = open('/var/www/lk/logs/nonvalid.log', 'wb')
    f.writelines(txt)
    return render(req, 'lktest/log.html', {'txt': txt})    

@user_passes_test(me_check)
def noaction(req):
    txt = ''
    txt = delete_noaction()
    f = open('/var/www/lk/logs/noaction.log', 'wb')
    f.writelines(txt)
    return render(req, 'lktest/log.html', {'txt': txt})

@user_passes_test(me_check)
def forum_send(req):
    txt = ''
    txt = send_mails_forumonly()
    f = open('/var/www/lk/logs/send_mails_forumonly.log', 'wb')
    f.writelines(txt)
    return render(req, 'lktest/log.html', {'txt': txt})

@user_passes_test(me_check)
def forum_check(req):
    txt = ''
    txt = check_file_forumonly()
    f = open('/var/www/lk/logs/check_file_forumonly.log', 'wb')
    f.writelines(txt)
    return render(req, 'lktest/log.html', {'txt': txt})

@user_passes_test(me_check)
def forum_delete(req):
    txt = ''
    txt = delete_forumonly()
    f = open('/var/www/lk/logs/delete_forumonly.log', 'wb')
    f.writelines(txt)
    return render(req, 'lktest/log.html', {'txt': txt})

@user_passes_test(me_check)
def make_list(req):
    txt = ''
    txt = make_remind_list()
    f = open('/var/www/lk/logs/remind.log', 'wb')
    f.writelines(txt)
    return render(req, 'lktest/log.html', {'txt': txt})

@user_passes_test(me_check)
def send_remind(req):
    txt = send_remind_list()
    f = open('/var/www/lk/logs/remind.log', 'wb')
    f.writelines(txt)
    return render(req, 'lktest/log.html', {'txt': txt})

