# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import SuggestedSources, Pages, Covid19Information, KodaKVKKForms, KodaTeam, TgpAdvantures, EventSuggestions, KodaDiaries, SuggestedSitesType, SuggestedSites, TeachersDocuments, RemoteLearning, ilMilliEgitim


from django.contrib import admin

admin.site.register(SuggestedSources)
admin.site.register(TgpAdvantures)
admin.site.register(EventSuggestions)
admin.site.register(KodaDiaries)
admin.site.register(SuggestedSitesType)
admin.site.register(SuggestedSites)
admin.site.register(TeachersDocuments)
admin.site.register(RemoteLearning)
admin.site.register(ilMilliEgitim)
admin.site.register(KodaTeam)
admin.site.register(KodaKVKKForms)
admin.site.register(Pages)
admin.site.register(Covid19Information)