from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from entry.views import PostListView, PostDetailView, PostListByCategoryView, CategoryListView
from entry.feeds import LatestPostsFeed

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', PostListView.as_view(), name='home'),
    url(r'^post/(?P<slug>[-\w]+)$', PostDetailView.as_view(), name='post'),
    # url(r'^nyarlathotep/', include('nyarlathotep.foo.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^feed/', LatestPostsFeed(), name='feeds'),
    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^category/(?P<slug>[-\w]+)', PostListByCategoryView.as_view(), name="category"),
)

urlpatterns += staticfiles_urlpatterns()
