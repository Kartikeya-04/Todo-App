from django.http import HttpResponse
from django.shortcuts import render, redirect
from website.models import Student
def home(request):
    if request.method=='POST':
        check=request.POST['address']
        student1=Student(name='AAyu',college='IIT',age=20,is_active=True)
        student1.save()
        #or we can do
        #check=request.POST.get('address')
        print(check)
   
    
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def services(request):
    return render(request,'services.html')