from django.shortcuts import render

# Create your views here
from django.shortcuts import HttpResponse
import operator
def home(requests):
    return HttpResponse('<h1> This is the first page in my web</h1>')
    
def about(requests):
    return  HttpResponse('<h2> About me: Iam Hemanth Kumar currently persiung BE course from Vasavi college of engineering</h2>')

def Hobbies(requests):
    return HttpResponse('<h2> My Hobbies are: Browsing internet,watching Movies, Playing sports </h2>')

