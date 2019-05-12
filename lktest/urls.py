from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import user_passes_test


def me_check(user):
    return user.id == 1
    
urlpatterns = patterns('',

    url(r'^$', user_passes_test(me_check)(TemplateView.as_view(template_name='lktest/app_index.html')), name='app_index'),
    url(r'^email_ping/$', 'lktest.views.email_ping', name='ping'),
    url(r'^all_forms/$', 'lktest.views.all_forms', name='forms'),
    url(r'^some_page/$', 'lktest.views.some_page', name='smpg'),
    url(r'^inactive/$', 'lktest.views.inactive', name='inactive'),
  #  url(r'^some_page/$', user_passes_test(me_check)(TemplateView.as_view(template_name='lktest/test_page.html')), name='smpg'),
    url(r'^nonvalid/$', 'lktest.views.nonvalid', name='nonvalid'),
    url(r'^noaction/$', 'lktest.views.noaction', name='noaction'),
    url(r'^forum_send/$', 'lktest.views.forum_send', name='forum_send'),
    url(r'^forum_check/$', 'lktest.views.forum_check', name='forum_check'),
    url(r'^forum_delete/$', 'lktest.views.forum_delete', name='forum_delete'),
    url(r'^list/$', 'lktest.views.make_list', name='list'),
    url(r'^send/s', 'lktest.views.send_remind', name='send'),

)
