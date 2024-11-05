
from django.shortcuts import render
import re
import string


# Create your views here.
def home(request):
    return render(request,'main/home.html')
