from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import user_passes_test


def activation_check(user):
    return user.is_active
    
urlpatterns = patterns('',

    url(r'^$', 'lkforum.views.index', name='app_index'),
    url(r'^all/(\d+)/$', 'lkforum.views.topic', name='topic'),
    url(r'^all/$', 'lkforum.views.topics', name='topics'), 
    url(r'^my/$', 'lkforum.views.my_qns', name='my_qns'),
    url(r'^new/$', 'lkforum.views.new_qn', name='new_qn'),
    url(r'^answers/$', 'lkforum.views.answers', name='answers'),
    url(r'^answer/(\d+)/$', 'lkforum.views.answer', name='answer'),
)