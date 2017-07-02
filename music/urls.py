from django.conf.urls import url
from . import views

urlpatterns = [
    #/music/
    url(r'^$', views.home, name='home'),

    #/music/19
    url(r'^(?P<album_id>[0-9]+)/$', views.details, name='details'),
]
