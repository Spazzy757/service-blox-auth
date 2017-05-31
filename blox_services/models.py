# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from blox_users.models import Profile
# Create your models here.


class Services(models.Model):
    user = models.ManyToManyField(Profile)
