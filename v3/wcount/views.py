from django.shortcuts import render
from .forms import MyColleagues
def home_view(requests):
    context={}
    context['form']=MyColleagues()
    return render(requests,'wcount/home.html',context)

