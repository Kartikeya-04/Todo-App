
from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('home/',views.emp_home),
    path('addEmp/',views.add_emp),
    path('deleteEmp/<int:emp_id>/',views.del_emp),
    path('UpdateEmp/<int:emp_id>/',views.update_emp),
    path('UpdateActionEmp/<int:emp_id>/',views.updateAction_emp),
    path('testi/',views.testimonial),
    path('Feedback/',views.feedback),





]
