from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import FeedbackForm,EmpForm

# Create your views here.
def emp_home(request):
    emp=Employee.objects.all()
    return render(request,'emp/home.html',{
         'emp':emp
    })
def add_emp(request):
    if request.method=='POST':
            emp_id=request.POST.get('empid')
            emp_name=request.POST.get('empname')
            emp_phone=request.POST.get('empphone')
            emp_email=request.POST.get('empemail')
            emp_address=request.POST.get('empaddress')
            emp_address=request.POST.get('empaddress')
            emp_exp=request.POST.get('empexperience')
            emp_department=request.POST.get('empdept')
            emp_work=request.POST.get('empwork')
            # Save data into the database

            e=Employee()
            e.emp_id=emp_id
            e.name=emp_name
            e.phone=emp_phone
            e.email=emp_email
            e.address=emp_address
            e.exp=emp_exp
            e.department=emp_department
            if emp_work is None:
                 e.working=False
            else:
                 e.working=True
            e.save()
            print(e.name,e.email,e.working,e.department,e.phone)
            print('ended')
            return redirect('/emp/home/')



#tried data fetching from forms
    form=EmpForm()
    return render(request,'emp/emp_add.html',{'form':form})


def del_emp(request,emp_id):
     print(emp_id)
     Employee.objects.filter(emp_id=emp_id).delete()
     return render(request,'emp/home.html')


def update_emp(request,emp_id):
     print(emp_id)
     emp=Employee.objects.filter(emp_id=emp_id).first()
     return render(request,'emp/update.html',{
          'emp':emp
          
     })
     

def updateAction_emp(request,emp_id):
     print(emp_id)
     if request.method=='POST':
            Newemp=Employee.objects.filter(emp_id=emp_id).first()
            emp_id=request.POST.get('empid')
            emp_name=request.POST.get('empname')
            emp_phone=request.POST.get('empphone')
            emp_email=request.POST.get('empemail')
            emp_address=request.POST.get('empaddress')
            emp_address=request.POST.get('empaddress')
            emp_exp=request.POST.get('empexperience')
            emp_department=request.POST.get('empdept')
            emp_work=request.POST.get('empwork')
            # Save data into the database

            Newemp.emp_id=emp_id
            Newemp.name=emp_name
            Newemp.phone=emp_phone
            Newemp.email=emp_email
            Newemp.address=emp_address
            Newemp.exp=emp_exp
            Newemp.department=emp_department
            if emp_work is None:
                 Newemp.working=False
            else:
                 Newemp.working=True
            Newemp.save()
            emp=Employee.objects.all()
            print('ended')
            return render(request,'emp/home.html',{
                  'emp':emp
             })
    
     
def testimonial(request):
     tes=Testimonial.objects.all()
     return render(request,'emp/testi.html',{
          'testi':tes
     })
     
def feedback(request):
     if request.method=="POST":
          form=FeedbackForm(request.POST)
          if form.is_valid():
               print(form.cleaned_data['Email'])
               print('data is saved !')
          else:
               return render(request,'emp/feedback.html',{'form':form})

     else:
          form=FeedbackForm()
          return render(request,'emp/feedback.html',{
               'form':form
          })  

     


    
