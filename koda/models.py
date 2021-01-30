# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ckeditor.fields import RichTextField
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

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


class TeachersDocuments(models.Model):
    title = models.CharField(max_length=250, null=True, blank=True)
    header_image = models.ImageField(null=True, blank=True)
    header_content = models.CharField(max_length=250, null=True, blank=True)
    content = RichTextUploadingField(null=True,
                                     blank=True,
                                     external_plugin_resources=[(
                                         'youtube',
                                         '/static/vendor/ckeditor_plugins/youtube/youtube/',
                                         'plugin.js',
                                     )],
                                     )

    def __str__(self):
        return self.title
        

class RemoteLearning(models.Model):
    title = models.CharField(max_length=250, null=True, blank=True)
    header_image = models.ImageField(null=True, blank=True)
    header_title = models.CharField(max_length=250, null=True, blank=True)
    content = RichTextUploadingField(null=True,
                                     blank=True,
                                     external_plugin_resources=[(
                                         'youtube',
                                         '/static/vendor/ckeditor_plugins/youtube/youtube/',
                                         'plugin.js',
                                     )],
                                     )
    def __str__(self):
        return self.title


class EventSuggestions(models.Model):
    title = models.CharField(max_length=250, null=True, blank=True)
    header_image = models.ImageField(null=True, blank=True)
    header_content = models.CharField(max_length=250, null=True, blank=True)
    content = RichTextUploadingField(null=True,
                                     blank=True,
                                     external_plugin_resources=[(
                                         'youtube',
                                         '/static/vendor/ckeditor_plugins/youtube/youtube/',
                                         'plugin.js',
                                     )],
                                     )

    def __str__(self):
        return self.title


class KodaDiaries(models.Model):
    title = models.CharField(max_length=250, null=True, blank=True)
    content = RichTextUploadingField(null=True,
                                     blank=True,
                                     external_plugin_resources=[(
                                         'youtube',
                                         '/static/vendor/ckeditor_plugins/youtube/youtube/',
                                         'plugin.js',
                                     )],
                                     )
    author = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title


class SuggestedSitesType(models.Model):
    site_name = models.CharField(max_length=250)

    def __str__(self):
        return self.site_name


class SuggestedSites(models.Model):
    title = models.CharField(max_length=250)
    site_type = models.ForeignKey(SuggestedSitesType, on_delete=models.CASCADE)
    url = models.URLField()

    def __str__(self):
        return self.title


class ilMilliEgitim(models.Model):
    content = RichTextUploadingField(null=True,
                                     blank=True,
                                     external_plugin_resources=[(
                                         'youtube',
                                         '/static/vendor/ckeditor_plugins/youtube/youtube/',
                                         'plugin.js',
                                     )],
                                     )



class KVKKForm(models.Model):
    title = models.SlugField(max_length=250)
    content = RichTextUploadingField(null=True,
                                     blank=True,
                                     external_plugin_resources=[(
                                         'youtube',
                                         '/static/vendor/ckeditor_plugins/youtube/youtube/',
                                         'plugin.js',
                                     )],
                                     )
