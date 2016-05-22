
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^preorder/$', views.order, name='order'),
    url(r'^process/$', views.process, name='process'),
]
