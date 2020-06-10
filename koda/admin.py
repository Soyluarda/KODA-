# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import SuggestedSources, TgpAdvantures, EventSuggestions, KodaDiaries, SuggestedSitesType, SuggestedSites

from django.contrib import admin

admin.site.register(SuggestedSources)
admin.site.register(TgpAdvantures)
admin.site.register(EventSuggestions)
admin.site.register(KodaDiaries)
admin.site.register(SuggestedSitesType)
admin.site.register(SuggestedSites)
