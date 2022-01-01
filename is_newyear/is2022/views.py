from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
import datetime

# Create your views here.


def is_newyear(request):
    now = datetime.datetime.now()
    return render(request, "is_newyear/index.html", {
        "newyear": now.month == 1 and now.day == 1
    })
