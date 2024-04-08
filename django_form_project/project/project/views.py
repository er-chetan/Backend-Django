from django.http import HttpRequest, HttpResponse
from django.template import loader
from django.shortcuts import render
from project.models import Student

def getform(request):
    return render(request,"get.html")

def postform(request):
    return render(request,"post.html")

def result(request):
    first=request.POST["first"]
    last=request.POST["last"]
    number=request.POST["number"]
    
    stu = Student(firstname=first, lastname=last, number=number)
    stu.save()

    return render(request,"result.html",{'first':first,'last':last,'number':number})


def fetchdata(request):
    mydata=Student.objects.all()
    template= loader.get_template('fetch_data.html')
    context = {'students_all':mydata}

    return HttpResponse(template.render(context, request))