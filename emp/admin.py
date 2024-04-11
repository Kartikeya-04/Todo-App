from django.contrib import admin
from .models import Employee,Testimonial
# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name','email','working')
    list_editable=('working',)
    search_fields = ['name','emp_id']
    list_filter=('department',)
admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Testimonial)

