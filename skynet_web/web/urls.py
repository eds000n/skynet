from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'runAlgs$', views.runAlgs, name='runAlgs'),
    url(r'^$', views.index, name='index'),
]
