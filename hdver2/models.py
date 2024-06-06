from django.db import models
from django.contrib.auth.models import User


class Ticket(models.Model):
    text = models.TextField()
    employee = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='employee_tickets')
    specialist = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='specialist_tickets')
    date_opened = models.DateTimeField()
    date_closed = models.DateTimeField(blank=False, null=True)
    priority = models.IntegerField(default=3)
    is_closed = models.BooleanField(default=0)

    class Meta:
        ordering = ["is_closed", "-date_opened", "-priority"]

