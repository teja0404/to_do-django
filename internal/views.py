from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Create your views here.

def index(request):

    content={"variable":"hello world"}
    return render(request,'internal\index.html',content)
