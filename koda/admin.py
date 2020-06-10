# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import SuggestedSources, TgpAdvantures, EventSuggestions, KodaDiaries

from django.contrib import admin

admin.site.register(SuggestedSources)
admin.site.register(TgpAdvantures)
admin.site.register(EventSuggestions)
admin.site.register(KodaDiaries)