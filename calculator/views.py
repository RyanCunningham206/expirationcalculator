from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def home_page(request):
    return render(request, 'calculator/basic.html')

def calculate(request):
    print("haha")
    return redirect("/")

