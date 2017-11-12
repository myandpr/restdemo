# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    birth = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ('birth',)


