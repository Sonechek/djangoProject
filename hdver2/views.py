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
        ticket.employee_id = request.user.id
        ticket.date_opened = datetime.datetime.now()
        ticket.save()

    return HttpResponseRedirect("/form")


def ticket(request):
    tickets = Ticket.objects.all()
    return render(request, 'hd/tickets.html', {"tickets": tickets})


def delete(request, id):
    try:
        ticket = Ticket.objects.get(id=id)
        ticket.delete()
        return HttpResponseRedirect("/tickets")
    except Ticket.DoesNotExist:
        return HttpResponseRedirect("<h2>Заявка не найдена</h2>")


def edit(request, id):
    try:
        ticket = Ticket.objects.get(id=id)
        if request.method == "POST":
            ticket.text = request.POST.get("text")
            ticket.date_closed = datetime.datetime.now()
            ticket.save()
            return HttpResponseRedirect("/tickets")
        else:
            return render(request, "hd/edit.html", {'ticket': ticket})
    except Ticket.DoesNotExist:
        return HttpResponseRedirect("<h2>Заявка не найдена</h2>")


def close_ticket(request, id):
    try:
        ticket = Ticket.objects.get(id=id)
        ticket.is_closed = True
        ticket.date_closed = datetime.datetime.now()
        ticket.save()
        return HttpResponseRedirect("/tickets")
    except Ticket.DoesNotExist:
        return HttpResponseRedirect("<h2>Заявка не найдена</h2>")