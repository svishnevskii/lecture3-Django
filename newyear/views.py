from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt

# Create your views here.
def index(request):
    now = dt.datetime.now()
    return render(request, "newyear/index.html", {
        'newyear': now.day == 21 and now.month == 8,
    })
