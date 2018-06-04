from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("hello,how are you?? ")

def insert(request):
    text = "hello"
    return render(request,'firstapp/display.html',{'text':text})
