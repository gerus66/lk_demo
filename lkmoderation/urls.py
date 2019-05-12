from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lk.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'lkmoderation.views.index', name='app_index'),
    url(r'^newf/(\d+)/$', 'lkmoderation.views.new_syn_mform', name='new_syn_mform'),
    url(r'^newf/$', 'lkmoderation.views.new_mform', name='new_mform'),
    url(r'^newq/$', 'lkmoderation.views.new_mquestion', name='new_mquestion'),
    url(r'^sfdelete/(\d+)/$', 'lkmoderation.views.sfdelete', name='sfdelete'),
    url(r'^sqdelete/(\d+)/$', 'lkmoderation.views.sqdelete', name='sqdelete'),
    url(r'^askmod/(\d+)/(\d+)/$', 'lkmoderation.views.askmod', name='askmod'),
    url(r'^showform/(\d+)/$', 'lkmoderation.views.showform', name='showform'),
    url(r'^modform/$', 'lkmoderation.views.modform', name='modform'),
    url(r'^modqn/$', 'lkmoderation.views.modqn', name='modqn'),
    url(r'^readform/$', 'lkmoderation.views.readform', name='readform'),

)
