from django.urls import path
from . import views

app_name = 'chatbot'  # Set the app namespace

urlpatterns = [
    path('', views.chatbot, name='chatbot'),
    # Add other URLs for the chatbot app here if needed
]
