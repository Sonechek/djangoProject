import datetime

from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Ticket



# Create your views here.

def index(request):
    return render(request, 'hd/index.html')

def form(request):
    tickets = Ticket.objects.all()
    return render(request, 'hd/form.html', {"tickets": tickets})


def create(request):
    if request.method == "POST":
        ticket = Ticket()
        ticket.text = request.POST.get("text")
        ticket.employee_id = request.POST.get("employee_id")
        ticket.specialist_id = request.POST.get("specialist_id")
        ticket.date_opened = datetime.datetime.now()
        ticket.date_closed = request.POST.get("date_closed")
        ticket.priority = request.POST.get("priority")
        ticket.save()
    return HttpResponseRedirect("/form")


def redirect(request):

    return render(request, "hd/../registration/login.html")
