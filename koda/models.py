# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ckeditor.fields import RichTextField
from django.db import models


class TgpAdvantures(models.Model):
    title = models.CharField(max_length=250, null=True, blank=True)
    youtube_url = models.URLField(max_length=250, null=True, blank=True)
    pdf = models.URLField(max_length=250, null=True, blank=True)
    mp3 = models.URLField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.title


class SuggestedSources(models.Model):
    title = models.CharField(max_length=250, null=True, blank=True)
    header_image = models.ImageField(null=True, blank=True)
    youtube_url = models.URLField(max_length=250, null=True, blank=True)
    pdf = models.URLField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.title

"""
class TeachersDocuments(models.Model):
    title = models.CharField(max_length=250, null=True, blank=True)
    header_image = models.ImageField(null=True, blank=True)
    header_content = models.CharField(max_length=250, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    pdf = models.URLField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.title
        
        

class RemoteLearning(models.Model):
    title = models.CharField(max_length=250, null=True, blank=True)
    header_image = models.ImageField(null=True, blank=True)
    header_title = models.CharField(max_length=250, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    pdf = models.URLField(max_length=250, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title

"""

class EventSuggestions(models.Model):
    title = models.CharField(max_length=250, null=True, blank=True)
    header_image = models.ImageField(null=True, blank=True)
    content = RichTextField(null=True, blank=True)
    pdf = models.URLField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.title


class KodaDiaries(models.Model):
    title = models.CharField(max_length=250, null=True, blank=True)
    header_image = models.ImageField(null=True, blank=True)
    content = RichTextField(null=True, blank=True)
    author = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title