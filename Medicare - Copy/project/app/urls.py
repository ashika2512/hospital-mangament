from django.contrib import admin
from django.urls import path,include
from app import views

urlpatterns = [
   
   path('',views.index,name='index'),
   path('register',views.register,name='register'),
   path('contact',views.contact,name='contact'),
   path('login',views.handlelogin,name='handlelogin'),
   path('about',views.about,name='about'),
   path('dashboard',views.dashboard,name='dashboard'),
   path('services',views.services,name='services'),
   path('our_doctors',views.our_doctors,name='our_doctors'),
   path('appointment',views.appointment,name='appointment'),
   path('handlelogout',views.handlelogout,name='handlelogout'),
   path('receptionist',views.receptionist,name='receptionist')
   
   
   
   
   
  


]