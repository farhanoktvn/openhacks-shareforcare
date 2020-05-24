from . import views
from django.urls import path

urlpatterns = [
    path('login/', views.accountLogin, name='accountLogin'),
    path('signup/', views.accountSignup, name='accountSignup'),
    path('logout/', views.accountSignout, name='accountSignout'),
]
