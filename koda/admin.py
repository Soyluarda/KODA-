# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import SuggestedSources, OgretmenTopluluklariYorumlari, KoyeİlkAdimVideolar, KoyeİlkAdimYorumlari, Pages, KodaConsultants, KodaTrainers, BiaIcerikler, KodaKVKKForms, KodaTeam, TgpAdvantures, EventSuggestions, KodaDiaries, SuggestedSitesType, SuggestedSites, TeachersDocuments, RemoteLearning, ilMilliEgitim


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
admin.site.register(BiaIcerikler)
admin.site.register(KodaConsultants)
admin.site.register(KodaTrainers)
admin.site.register(OgretmenTopluluklariYorumlari)
admin.site.register(KoyeİlkAdimYorumlari)
admin.site.register(KoyeİlkAdimVideolar)
