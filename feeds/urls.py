from django.urls import path
from . import views

app_name = 'feeds'
urlpatterns = [
    path('',views.home_page,name="main_home" ),
]