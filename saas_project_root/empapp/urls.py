from django.urls import path

from . import views

urlpatterns = [
    path('employee/', views.create_employee),
    path('list_emp/', views.list_employees),
    path('del_emp/', views.del_emp_form),
    path('ems/', views.ems),
    path('update_employee/<pk>',views.update_employee, name='update_employee'),
    path('delete_employee/<pk>/', views.delete_employee, name='delete_employee'),


]