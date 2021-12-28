from django.conf.urls import url
from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

# what does url patterns do?
"""
In django, views are python functions which take URL request 
as parameter and return an HTTP response or throw and exception 404

Each view is mapped to a corresponding URL pattern. This is done via
python module called URLConf(URL configuration).


"""

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('<str:pk>', views.go, name='go')
]