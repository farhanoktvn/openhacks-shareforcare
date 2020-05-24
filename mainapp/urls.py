from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('needs/', views.needsList, name='needs'),
    path('need/<id>', views.needDetail, name='need_detail'),
    path('extras/', views.extrasList, name='extras'),
    path('extra/<id>', views.extraDetail, name='extra_detail'),
]
