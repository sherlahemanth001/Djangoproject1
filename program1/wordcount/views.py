from django.shortcuts import HttpResponse
from django.shortcuts import render
import operator
def home(requests):
    return render(requests,'wordcount/home.html', {'name':'Hemanth'})
def aboutus(requests):
    return render(requests,'wordcount/about.html', {'userid':'sherlahemanth001'})


