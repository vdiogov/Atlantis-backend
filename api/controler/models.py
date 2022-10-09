from datetime import date
import numbers
from socket import NI_NUMERICHOST
from sys import get_coroutine_origin_tracking_depth
from xmlrpc.client import DateTime
from django.db import models
from django.contrib.auth.models import User

class Queue(models.Model):
    numero = models.CharField(max_length=8)
    atendente = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    guiche = models.CharField(max_length=8)
    buzz = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class QueueSpecial(models.Model):
    numero = models.CharField(max_length=8)
    atendente = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    guiche = models.CharField(max_length=8)
    buzz = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)