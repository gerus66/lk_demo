from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.utils import timezone, translation
from lkforms.models import Form, UserProfile, Answer, RegRes
from lkforms.views import make_structure, set_external, make_result, make_diplom, compare_lists, check_test, base_forms, send_all
from django.contrib.auth.decorators import user_passes_test


def staff_check(user):
    return user.is_staff

def activation_check(user):
    return user.is_active
    
@user_passes_test(staff_check)        
def download(req, file_type, file_name):
    if file_type == 'txt':
        f = Form.objects.get(id=file_name[:file_name.find('.')])
        f.make_txt()
    elif file_type == 'profiles':
        u = UserProfile.objects.get(id=file_name[:file_name.find('_')])
        u.make_profile()	
    elif file_type == 'structure':
        make_structure()
    elif file_type == 'send_all':
        send_all(file_name)
    elif file_type == 'set_external':
        file_type = 'external'
        set_external(req, file_name, 'set')
    elif file_type == 'send_external':
        file_type = 'external'
        set_external(req, file_name, 'send')
    elif file_type == 'find_external':
        file_type = 'external'
        set_external(req, file_name, 'find')
    elif file_type == 'result':
        if req.user.is_superuser or req.user == Form.objects.get(id=file_name[:file_name.find('_')]).owner or req.user in Form.objects.get(id=file_name[:file_name.find('_')]).editor.all():
            make_result(file_name)
        else:
            return HttpResponseRedirect(req.META['HTTP_REFERER'])
    elif file_type == 'diploms_result':
        file_type = 'result'
        make_diplom(file_name)
    elif file_type == 'default':
        compare_lists(file_name)
    elif file_type == 'answers':
        check_test(file_name)
    elif file_type[:4] == 'read':
        f = open('/var/www/lk/media/' + file_type[5:] + '/' + file_name, 'rb')
        return HttpResponse(f, content_type='application/octet-stream')
    f = open('/var/www/lk/media/' + file_type + '/' + file_name, 'rb')
    return HttpResponse(f, content_type='application/octet-stream')

@user_passes_test(activation_check)
def index(req):
    br = []
    for rr in RegRes.objects.filter(user=req.user.profile.all()[0]):
        if rr.form.id in base_forms:
            br.append(rr.form)
    return render(req, 'index.html', {'br': br})

def lang(req, code):
    translation.activate(code)
    req.session[translation.LANGUAGE_SESSION_KEY] = code
#    full_path = req.get_full_path()
#    try:
 #       full_path = req.META['HTTP_REFERER']
#        current_path = full_path[full_path.index('/', 1):]
#    except KeyError:
#        full_path = '/'
 #       current_path = '/'
 #   next = req.META['HTTP_REFERER']
    return HttpResponseRedirect('/')
    
