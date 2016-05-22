
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^en/$', views.index_en, name='index_en'),
    url(r'^fr/$', views.index_fr, name='index_fr'),
    url(r'^preordenar/$', views.order, name='order'),
    url(r'^en/preorder/$', views.order_en, name='order_fr'),
    url(r'^fr/preorder/$', views.order_fr, name='order_fr'),
    url(r'^process/$', views.process, name='process'),
]
