from django.shortcuts import render

# Create your views here
from django.shortcuts import HttpResponse
import operator
def home(requests):
    return HttpResponse('<h1> This is the first page in my web</h1>')
