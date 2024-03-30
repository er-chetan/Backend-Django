from django.http import HttpRequest
from django.shortcuts import render

def calculator(request):
    name = request.POST["name"]
    age = request.POST["age"]
    return render(request,'calculator.html',{'name':name,'age':age})

def sampleform(request):
    return render(request,'sampleform.html')