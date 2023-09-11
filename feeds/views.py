from django.shortcuts import render
from .models import *

# Create your views here.


def home_page(request):
    context = {

    }

    return render(request, 'home_page.html', context)
