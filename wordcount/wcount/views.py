from django.shortcuts import render
import operator
from django.http import HttpResponse

def home(requests):
    return render(requests, 'wcount/home.html')

def count(requests):
    mytext=requests.GET['fulltext']  
    wcount=len(mytext.split())
    mylist=[('rn1','Amar'),('rn2','Srinivas'),('rn3','Ram'),('rn4','Shyam')]
   
    return render(requests, 'wcount/count.html',{'mycount':wcount ,'yourlist':mylist}
)


