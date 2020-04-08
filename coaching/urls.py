from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('contact/',views.contact,name='contact'),
    path('galeri/', views.galeri, name='galeri'),
    path('about/', views.about, name='about'),
    path('team/', views.team, name='team'),
    path('products/',views.products,name='products'),
    path('index2/',views.index2,name='index2'),
    path('basvuru/', views.basvuru, name='basvuru'),
    path('bagis/', views.bagis, name='bagis'),
    path('gonullu/', views.gonullu, name='gonullu'),
    path('bize-katilin/', views.bize_katilin, name='bize_katilin'),
    path('koda-gonullusu/', views.koda_gonullusu, name='koda_gonullusu'),
    path('yayinlarimiz/', views.yayinlarimiz, name='yayinlarimiz'),
    path('koda-ile-isbirligi/', views.isbirligi, name='isbirligi'),
    path('sponsor-olmak/', views.sponsor, name='sponsor'),
    path('bagis-detay/', views.bagis_detay, name='bagis_detay'),
    path('neler-yapmiyoruz/', views.neler_yapmiyoruz, name='neler_yapmiyoruz'),
    path('koy-ogretmenleri-projesi/', views.koy_ogretmenleri, name='koy_ogretmenleri'),
    path('stratejimiz/', views.stratejimiz, name='stratejimiz'),
    path('faaliyet-raporlari/', views.faaliyet_raporlari, name='faaliyet_raporlari'),
    path('ogretmen-topluluklari/', views.ogretmen_topluluklari, name='ogretmen_topluluklari'),
    path('bsmg-programi/', views.bsmg_programi, name='bsmg_programi'),
    path('mentorluk-programi/', views.mentorluk_programi, name='mentorluk_programi'),
    path('cocuk-atolyeleri/', views.cocuk_atolyeleri, name='cocuk_atolyeleri'),
    path('gecmis-faaliyetler/', views.gecmis_faaliyetler, name='gecmis_faaliyetler'),
    path('degerlerimiz/', views.degerlerimiz, name='degerlerimiz'),
    path('ruzgargulubultenleri/', views.ruzgargulubultenleri, name='ruzgargulubultenleri'),
    path('koda-raporlari/', views.koda_raporlari, name='koda_raporlari'),
    path('kurumsal-destek/', views.kurumsal_destek, name='kurumsal_destek'),
    path('koda-haritasi/', views.koda_haritasi, name='koda_haritasi'),

]
