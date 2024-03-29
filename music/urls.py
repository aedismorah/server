from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<album_id>[0-9]+)/(?P<song>[ -z]+)/$', views.play, name='play'),
    url(r'^(?P<album_id>[0-9]+)/stop/$', views.stop, name='stop'),
]
