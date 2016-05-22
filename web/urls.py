
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^order/', views.order, name='order'),
    url(r'^$', views.index, name='index'),
]
