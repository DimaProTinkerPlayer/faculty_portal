from django.urls import path
from . import views
from django.contrib import admin

app_name = 'faculty'

urlpatterns = [
    path('', views.index, name='index'),
    path('programs/', views.program_list, name='program_list'),
    path('programs/<int:pk>/', views.program_detail, name='program_detail'),
    path('departments/', views.department_list, name='department_list'),
    path('departments/<int:pk>/', views.department_detail, name='department_detail'),
    path('exchanges/', views.exchange_list, name='exchange_list'),
    ]