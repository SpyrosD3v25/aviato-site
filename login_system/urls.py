from django.urls import path
from . import views

urlpatterns = [
    path('sign-up/', views.signup_view, name='signup'),
    path('sign-in/', views.login_view, name='login'),
]
