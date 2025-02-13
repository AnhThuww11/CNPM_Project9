# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def Courses(request):
    return HttpResponse("Hello world!")
def Student(request):
    return HttpResponse("Hello world!")