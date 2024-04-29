import datetime

from django.db import models


# Create your models here.


class Ticket(models.Model):
    text = models.TextField()
    employee = models.IntegerField()
    specialist = models.IntegerField()
    date_opened = models.DateTimeField()
    date_closed = models.DateTimeField(blank=False, null=True)
    priority = models.IntegerField(default=3)
    is_closed = models.BooleanField(default=0)

    class Meta:
        ordering = ["is_closed", "-date_opened"]