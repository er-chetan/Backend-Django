from django.http import HttpRequest
from django.shortcuts import render

def getform(request):
    return render(request,"get.html")

def postform(request):
    return render(request,"post.html")

def result(request):
    first=request.POST["first"]
    last=request.POST["last"]
    number=request.POST["number"]
    return render(request,"result.html",{'first':first,'last':last,'number':number})