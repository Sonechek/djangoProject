import datetime

from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
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
        ticket.employee = request.POST.get("employee")
        ticket.specialist = request.POST.get("specialist")
        ticket.date_opened = datetime.datetime.now()
        ticket.save()
    return HttpResponseRedirect("/form")


from django.views import generic

class TicketListView(generic.ListView):
    model = Ticket
