from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.PostView.as_view(), name='post_list'),
    url(r'^new/$', views.post_new, name='post_new'),
]