from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import user_passes_test


def activation_check(user):
    return user.is_active
    
urlpatterns = patterns('',

   # url(r'^$', user_passes_test(activation_check)(TemplateView.as_view(template_name='lkforms/app_index.html')), name='app_index'),
  #  url(r'^forms/$', 'lkforms.views.forms', name='forms'),
    url(r'^$', 'lkforms.views.forms', name='forms'),
    url(r'^form/(\d+)/$', 'lkforms.views.form', name='form'),
    url(r'^form/(\d+)/reverse/$', 'lkforms.views.reverse', name='reverse'), 
    url(r'^form/(\d+)/result/$', 'lkforms.views.result', name='result'),
    url(r'^structure/$', 'lkforms.views.structure', name='structure'),
    url(r'^download/([\w.]+)/([\w.]+)/?$', 'lkforms.views.download'),
    url(r'^showform/(\d+)/$', 'lkforms.views.showform', name='showform'),
    url(r'^qn/(\d+)/toarch/$', 'lkforms.views.qn_to_archive', name='qn_to_archive'),
    url(r'^form/(\d+)/regtoarch/$', 'lkforms.views.reg_to_archive', name='reg_to_archive'),
    url(r'^form/(\d+)/restoarch/$', 'lkforms.views.res_to_archive', name='res_to_archive'),
    url(r'^external/new/$', 'lkforms.views.new_external', name='new_external'),
    url(r'^userprofile/delete_email/(\d+)/$', 'lkforms.views.delete_email', name='delete_email'),
    url(r'^form/generate_mm/$', 'lkforms.views.generate_mm', name='generate_mm'),
)
