from django.db import models


# Create your models here.


class Ticket(models.Model):
    text = models.TextField()
    employee_id = models.IntegerField()
    specialist_id = models.IntegerField()
    date_opened = models.DateTimeField()
    date_closed = models.DateTimeField()
    priority = models.IntegerField()
