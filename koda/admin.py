# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import TeachersDocuments, SuggestedSources, TgpAdvantures, EventSuggestions, RemoteLearning

from django.contrib import admin

admin.site.register(TeachersDocuments)
admin.site.register(SuggestedSources)
admin.site.register(TgpAdvantures)
admin.site.register(EventSuggestions)
admin.site.register(RemoteLearning)
