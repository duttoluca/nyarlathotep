from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import ListView, DetailView

from entry.models import Post

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    url(r'^$', ListView.as_view(model=Post,
                                queryset=Post.objects.get_visible(),
                                paginate_by=5), name='home'),
    url(r'^post/(?P<slug>[-\w]+)$', DetailView.as_view(model=Post,
                                                       queryset=Post.objects.get_visible()), name='post'),
    # url(r'^nyarlathotep/', include('nyarlathotep.foo.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
