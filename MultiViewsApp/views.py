from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def f1(request):
    return HttpResponse("<h2>Hello User<br/>Welcome TO DJANGO MultiViewsApp of f1()</h2>");
def f2(request):
    return HttpResponse("<h2>Hello User<br/>Welcome TO DJANGO MultiViewsApp of f2()</h2>");
def f3(request):
    return HttpResponse("<h2>Hello User<br/>Welcome TO DJANGO MultiViewsApp of f3()</h2>");
def no(request):
    ss='''<h2>HelloUser<br/>Please try with another url<br/>It helps you to reach the page you need<br/>
       <h2 style='color:Green;'> This may occur beacuse you have enter wrong url OR Unknown url</h2></h2>'''
    return HttpResponse(ss);

