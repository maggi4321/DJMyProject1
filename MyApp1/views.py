from django.shortcuts import render
from django.http import HttpResponse

# create your views here.
def display(request):
    ss="<center><h2> Hello User <br/> Welcome to DJango Project in Pycharm</h2></center>"
    return HttpResponse(ss)

def show(request):
    ss='''<html>
    <head> <title>Welcome Page </title>
    <style>
        h3{ color:Green; }
    </style>
    </head>
    <body>
    <center>
    <h1>Welcome to Django</h2>
    <hr/>
    <h2>Welcome to Django</h2>
    <hr/
    <h3>Welcome to Django</h3>
    <hr color='Green'/>
    <h4>Welcome to Django</h4>
    <hr/>
    <h5>Welcome to Django</h5>
    </center>
    </body>
    <html>'''
    return HttpResponse(ss)