from django.db import models
import datetime
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import User


class Task(models.Model):
    PRIORITY_CHOICES = [
        ("low", "Low"),
        ("middle", "Middle"),
        ("urgent", "Urgent"),
    ]

    title = models.CharField(max_length=30)
    description = models.CharField(max_length=500)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, null=True)
    due_date = models.DateField(default=datetime.date.today)
    category = models.ForeignKey("Category", on_delete=models.CASCADE, null=True)
    assigned_users = models.ManyToManyField(User, related_name="tasks")
    subtasks = models.JSONField(default=list)
    state = models.CharField(max_length=20, null=True)


class User(AbstractBaseUser):
    identifier = models.CharField(max_length=40, unique=True)
    USERNAME_FIELD = "identifier"



class Category(models.Model):
    name = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
