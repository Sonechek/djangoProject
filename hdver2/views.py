import datetime

from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from .models import Ticket


def index(request):
    return render(request, 'hd/index.html')


@login_required
def form(request):
    tickets = Ticket.objects.all()
    return render(request, 'hd/form.html', {"tickets": tickets})


def create(request):
    if request.method == "POST":
        ticket = Ticket()
        ticket.text = request.POST.get("text")
        ticket.specialist = request.POST.get("specialist")
        ticket.date_opened = datetime.datetime.now()
        ticket.save()
    return HttpResponseRedirect("/form")
