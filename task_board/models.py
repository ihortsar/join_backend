from django.conf import settings
from django.db import models
import datetime

class Task(models.Model):
    title = models.CharField(default=None,max_length=30)
    description = models.CharField(default=None,max_length=500)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    urgent = models.BooleanField(default=False)
    middle = models.BooleanField(default=False)
    low = models.BooleanField(default=True)
    due_date = models.DateField("Date", default=datetime.date.today)
