from django.contrib import admin
from django.urls import path
from . import views


app_name = 'pdf'

urlpatterns = [
    path('', views.accept, name = 'accept'),
    path('<int:id>/', views.resume, name = 'resume'),
    path('list/', views.resume_list, name = 'resume_list'),
]
