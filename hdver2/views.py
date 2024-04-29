import datetime

from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Ticket


def index(request):
    return render(request, 'hd/index.html')


def form(request):
    tickets = Ticket.objects.all()
    return render(request, 'hd/form.html', {"tickets": tickets})


def create(request):
    if request.method == "POST":
        ticket = Ticket()
        ticket.text = request.POST.get("text")
        ticket.employee = request.POST.get("employee")
        ticket.specialist = request.POST.get("specialist")
        ticket.date_opened = datetime.datetime.now()
        ticket.save()
    return HttpResponseRedirect("/form")
