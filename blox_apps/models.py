# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from blox_users.models import User
from blox_services.models import Services
# Create your models here.


class App(models.Model):
    token = models.CharField(max_length=200, db_index=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    services = models.ManyToManyField(Services)
