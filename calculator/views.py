from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime

# Create your views here.


class Expiry:
    def __init__(self, entries):
        self.entries = entries

    def finaldate(self):
        today = datetime.datetime.now()
        final_date = today + self.entries
        return final_date


weeks = 0
days = 0
hours = 0

time = Expiry(datetime.timedelta(weeks=weeks, days=days, hours=hours))

def home_page(request):
    return render(request, 'calculator/basic.html')


def calculate(request):
    global weeks
    global days
    global hours
    if request.method == 'POST':
        if request.POST.get('weeks') == "":
            weeks = 0
        else:
            weeks = request.POST.get('weeks')
        if request.POST.get('days') == "":
            days = 0
        else:
            days = request.POST.get('days')
        if request.POST.get('hours') == "":
            hours = 0
        else:
            hours = request.POST.get('hours')
    return redirect("/solution")

def solution(request):
    global weeks
    today = datetime.datetime.now()
    final_date = today + datetime.timedelta(weeks=int(weeks), days=int(days), hours=int(hours))
    print(final_date)
    return HttpResponse("Expiration Date:"
                        "%s " % final_date)



