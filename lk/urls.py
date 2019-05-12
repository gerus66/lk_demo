from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.views.generic.base import RedirectView, TemplateView
from django.contrib.auth.decorators import user_passes_test


def activation_check(user):
    return user.is_active

urlpatterns = patterns('',
    url(r'^i18n/', include('django.conf.urls.i18n')),   
    url(r'^admin/download/([\w.]+)/([\w.]+)/?$', 'lk.views.download'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^lk/lang/([a-z]{2})/?$', 'lk.views.lang', name='lang'),
)
    
urlpatterns += i18n_patterns('',
    # Examples:
    # url(r'^$', 'lk.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', RedirectView.as_view(url='/lk/')),
    url(r'^lk/test/?', include('lktest.urls', namespace='lktest')),
    url(r'^lk/forms/?', include('lkforms.urls', namespace='lkforms')),
    url(r'^lk/forum/?', include('lkforum.urls', namespace='lkforum')),
    url(r'^lk/mod/?', include('lkmoderation.urls', namespace='lkmoderation')),
    url(r'^lk/faq/?', TemplateView.as_view(template_name='faq.html'), name='faq'),
  #  url(r'^lk/?', user_passes_test(activation_check)(TemplateView.as_view(template_name='index.html')), name='index'),   
    url(r'^lk/?', 'lk.views.index', name='index'),
    url(r'^accounts/?', include('lkregistration.backends.default.urls')),
#    url(r'^admin/download/([\w.]+)/([\w.]+)/?$', 'lk.views.download'),
#    url(r'^admin/', include(admin.site.urls)),
)


