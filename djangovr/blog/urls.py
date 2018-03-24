# blog/urls.py

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^service$', views.introduce_service, name='introduce_service'),
    url(r'^introduction$', views.introduce_voithru, name='introduce_voithru'),
    url(r'^helpdesk/$', views.help_list, name='help_list'),
    # url(r'^helpdesk/(?P<pk>\d+)/$', views.help_detail, name='help_detail'),
    url(r'^helpdesk/new/$', views.help_new, name='help_new'),
]
