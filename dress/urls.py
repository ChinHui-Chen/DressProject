from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
from dress_pool.views import post_dress
from django.core.urlresolvers import reverse
from django.views.generic.base import RedirectView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dress.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', RedirectView.as_view(url='/admin/dress_pool/dress')),
    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^dress/post/$', post_dress),
    #url(r'^list/$', Hello_World),
)




