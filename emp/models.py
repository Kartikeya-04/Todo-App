from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Employee(models.Model):
    emp_id=models.CharField(max_length=50)
    name=models.CharField(max_length=100)
    phone=models.IntegerField(max_length=10)
    email=models.CharField(max_length=15)
    address=models.CharField(max_length=300)
    exp=models.IntegerField(max_length=40)
    department=models.CharField(max_length=12)
    working=models.BooleanField(default=True)
    #FOR CUSTOMIZATION OF ADMIN !
    # def __str__(self):
    #     return (self.name +' - ' +self.department)

class Testimonial(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)

    name=models.CharField(max_length=200)
    content=models.TextField()
    picture=models.ImageField(upload_to='testimonial/')
    rating=models.IntegerField(max_length=1)

    def __str__(self):
        
        return (self.name +' - ' +str(self.rating))


