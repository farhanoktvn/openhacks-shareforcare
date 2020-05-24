from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('needs/', views.needsList, name='needs'),
    path('extras/', views.extrasList, name='extras'),
    path('post/<id>/', views.postDetail, name='post_detail'),
]
