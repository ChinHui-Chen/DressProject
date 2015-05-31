from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from dress_pool.views import post_dress

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dress.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^dress/post/$', post_dress),
    #url(r'^list/$', Hello_World),
)