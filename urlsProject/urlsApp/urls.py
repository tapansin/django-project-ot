from django.urls import path
from django.contrib import admin
from urlsApp import views


urlpatterns = [
    path('hydjobs/', views.hydjobsinfo),
    path('punejobs/', views.punejobsinfo),
    path('noidajobs/', views.noidajobsinfo),
    path('chennaijobs/', views.chennaijobsinfo),
]