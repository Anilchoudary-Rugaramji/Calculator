from django.urls import re_path
from calci_app import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^add$', views.addition, name='add'),
    re_path(r'^sub$', views.subtraction, name='sub'),
    re_path(r'^multi$', views.multiplication, name='multi'),
    re_path(r'^div$', views.division, name='div'),
]
