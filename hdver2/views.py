import datetime

from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required, permission_required
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

@permission_required('admin')
def ticket(request):
    tickets = Ticket.objects.all()
    return render(request, 'hd/tickets.html', {"tickets": tickets})


@permission_required('ticket.delete')
def delete(request, id):
    try:
        ticket = Ticket.objects.get(id=id)
        ticket.delete()
        return HttpResponseRedirect("/tickets")
    except Ticket.DoesNotExist:
        return HttpResponseRedirect("<h2>Заявка не найдена</h2>")


@permission_required('ticket.edit')
def edit(request, id):
    try:
        ticket = Ticket.objects.get(id=id)
        if request.method == "POST":
            ticket.text = request.POST.get("text")
            ticket.priority = request.POST.get("priority")
            ticket.save()
            return HttpResponseRedirect("/tickets")
        else:
            return render(request, "hd/edit.html", {'ticket': ticket})
    except Ticket.DoesNotExist:
        return HttpResponseRedirect("<h2>Заявка не найдена</h2>")


@permission_required('ticket.edit')
def close_ticket(request, id):
    try:
        ticket = Ticket.objects.get(id=id)
        ticket.is_closed = True
        ticket.date_closed = datetime.datetime.now()
        ticket.save()
        return HttpResponseRedirect("/tickets")
    except Ticket.DoesNotExist:
        return HttpResponseRedirect("<h2>Заявка не найдена</h2>")


@permission_required('admin')
def reports(request):
    tickets = Ticket.objects.all()
    today = datetime.datetime.now()
    if request.method == 'POST':
        tickets = Ticket.objects.filter(date_opened__range=(request.POST.get('start_date'), request.POST.get('end_date')))
        tickets_count = tickets.count()
        tickets_closed_count = 0
        for ticket in tickets:
            if ticket.is_closed:
                tickets_closed_count += 1
        return render(request, 'hd/reports.html', {'tickets': tickets, 'tickets_count': tickets_count, 'tickets_closed_count': tickets_closed_count})
    else:
        return render(request, 'hd/reports.html', {'ticket':tickets} )
