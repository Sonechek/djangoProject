import datetime

from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render
from .models import Ticket
from django.contrib.auth.models import User



def index(request):
    return render(request, 'hd/index.html')


@permission_required('hdver2.add_ticket')
def form(request):
    tickets = Ticket.objects.all()
    return render(request, 'hd/form.html', {"tickets": tickets})


@permission_required('hdver2.add_ticket')
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


@permission_required('admin')
def delete(request, id):
    try:
        ticket = Ticket.objects.get(id=id)
        ticket.delete()
        return HttpResponseRedirect("/tickets")
    except Ticket.DoesNotExist:
        return HttpResponseRedirect("<h2>Заявка не найдена</h2>")


@permission_required('admin')
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


@permission_required('admin')
def close_ticket(request, id):
    try:
        ticket = Ticket.objects.get(id=id)
        ticket.is_closed = True
        ticket.date_closed = datetime.datetime.now()
        ticket.specialist_id =  request.user.id
        ticket.save()
        return HttpResponseRedirect("/tickets")
    except Ticket.DoesNotExist:
        return HttpResponseRedirect("<h2>Заявка не найдена</h2>")


@permission_required('admin')
def reports(request):
    tickets = Ticket.objects.all()
    users = User.objects.all()
    tickets_count = tickets.count()
    tickets_closed_count = 0
    for ticket in tickets:
        if ticket.is_closed:
            tickets_closed_count += 1
    if request.method == 'POST':
        tickets = Ticket.objects.filter(date_opened__range=(request.POST.get('start_date'), request.POST.get('end_date')))
        tickets_count = tickets.count()
        tickets_closed_count = 0
        for ticket in tickets:
            if ticket.is_closed:
                tickets_closed_count += 1
        return render(request, 'hd/reports.html', {'tickets': tickets, 'tickets_count': tickets_count, 'tickets_closed_count': tickets_closed_count, 'users': users})
    else:
        return render(request, 'hd/reports.html', {'tickets': tickets, 'tickets_count': tickets_count, 'tickets_closed_count': tickets_closed_count})
