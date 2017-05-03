from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^lessons/$', views.lessons, name='lessons'),
    url(r'^lessons/(?P<pk>[0-9]+)/$', views.tuitor, name='tuitor'),
    url(r'^choose$', views.choose, name='choose'),
    url(r'^success/$', views.success, name='success'),
]
