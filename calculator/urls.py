from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('calculate/', views.calculate, name='calculate'),
    path('solution/', views.solution, name='solution'),
]