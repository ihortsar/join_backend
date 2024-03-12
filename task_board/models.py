from django.conf import settings
from django.db import models
import datetime



class Task(models.Model):
    PRIORITY_CHOICES = [
        ("low", "Low"),
        ("middle", "Middle"),
        ("urgent", "Urgent"),
    ]

    title = models.CharField(max_length=30)
    description = models.CharField(max_length=500)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default=None)
    due_date = models.DateField(default=datetime.date.today)
    category = models.JSONField(default=dict)
    assigned_users = models.JSONField(default=list)
    subtasks = models.JSONField(default=list)
