from django.shortcuts import render
def add(requests):
	render(requests,'mycontacts/add.html',{})
def show(requests):
	render(requests,'mycontacts/show.html',{})

# Create your views here.
