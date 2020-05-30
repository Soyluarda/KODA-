# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class TgpAdvantures(models.Model):
    title = models.CharField(max_length=250, null=True, blank=True)
    youtube_url = models.URLField(max_length=250, null=True, blank=True)
    pdf = models.FileField(upload_to='pdf', null=True, blank=True)


class SuggestedSources(models.Model):
    title = models.CharField(max_length=250, null=True, blank=True)
    youtube_url = models.URLField(max_length=250, null=True, blank=True)
    pdf = models.FileField(upload_to='pdf', null=True, blank=True)


class TeachersDocuments(models.Model):
    title = models.CharField(max_length=250, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    pdf = models.FileField(upload_to='pdf', null=True, blank=True)


class EventSuggestions(models.Model):
    title = models.CharField(max_length=250, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    pdf = models.FileField(upload_to='pdf', null=True, blank=True)


class RemoteLearning(models.Model):
    title = models.CharField(max_length=250, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    pdf = models.FileField(upload_to='pdf', null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

