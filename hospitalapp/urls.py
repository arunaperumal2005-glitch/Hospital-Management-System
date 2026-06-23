from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('login/',user_login,name='login'),
    path('logout/',user_logout,name='logout'),
    path('patients/',patient_list,name='patient_list'),
    path('doctors/',doctor_list,name='doctor_list'),
    path('appointments/',appointment_list,name='appointment_list'),
    path('patients/add/', add_patient, name='add_patient'),
    path('doctors/add/', add_doctor, name='add_doctor'),
    path('appointments/add/', add_appointment, name='add_appointment'),
    path('patients/edit/<int:pk>/', edit_patient, name='edit_patient'),
    path('patients/delete/<int:pk>/', delete_patient, name='delete_patient'),
    path('doctors/edit/<int:pk>/', edit_doctor, name='edit_doctor'),
    path('doctors/delete/<int:pk>/', delete_doctor, name='delete_doctor'),
    path('appointments/edit/<int:pk>/', edit_appointment, name='edit_appointment'),
    path('appointments/delete/<int:pk>/', delete_appointment, name='delete_appointment'),

]

