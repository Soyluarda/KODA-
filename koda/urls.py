from django.conf.urls import url
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('iletisim/',views.contact,name='contact'),
    path('galeri/', views.galeri, name='galeri'),
    path('hakkimizda/', views.about, name='about'),
    path('ekip/', views.team, name='team'),
    path('egitmenlerimiz/', views.trainers, name='trainers'),
    path('neler-yapiyoruz/',views.products,name='products'),
    path('basvuru/', views.basvuru, name='basvuru'),
    re_path(r'kvkk-forms/(?P<title>[\w-]+)/$', views.kvkk_detail, name='kvkk_detail'),
    path('nasil-destek-olabilirsiniz/', views.nasil_destek_olabilirsiniz, name='nasil_destek_olabilirsiniz'),
    path('gonullu/', views.gonullu, name='gonullu'),
    path('bize-katilin/', views.bize_katilin, name='bize_katilin'),
    path('koda-gonullusu/', views.koda_gonullusu, name='koda_gonullusu'),
    path('yayinlarimiz/', views.yayinlarimiz, name='yayinlarimiz'),
    path('koda-ile-isbirligi/', views.isbirligi, name='isbirligi'),
    path('sponsor-olmak/', views.sponsor, name='sponsor'),
    path('bagis-detay/', views.bagis_detay, name='bagis_detay'),
    path('bagis-yap/', views.bagis_yap, name='bagis_yap'),
    path('neler-yapmiyoruz/', views.neler_yapmiyoruz, name='neler_yapmiyoruz'),
    path('faaliyetlerimiz/', views.koy_ogretmenleri, name='faaliyetlerimiz'),
    path('stratejimiz/', views.stratejimiz, name='stratejimiz'),
    path('faaliyet-raporlari/', views.faaliyet_raporlari, name='faaliyet_raporlari'),
    path('ogretmen-topluluklari/', views.ogretmen_topluluklari, name='ogretmen_topluluklari'),
    path('bsmg-programi/', views.bsmg_programi, name='bsmg_programi'),
    path('mentorluk-programi/', views.mentorluk_programi, name='mentorluk_programi'),
    path('koye-ilk-adim/', views.koye_ilk_adim, name='koye_ilk_adim'),
    path('koye-ilk-adim-videolar/', views.koye_ilk_adim_videolar, name='koye_ilk_adim_videolar'),
    path('gecmis-faaliyetler/', views.gecmis_faaliyetler, name='gecmis_faaliyetler'),
    path('degerlerimiz/', views.degerlerimiz, name='degerlerimiz'),
    path('ruzgargulubultenleri/', views.ruzgargulubultenleri, name='ruzgargulubultenleri'),
    path('koda-raporlari/', views.koda_raporlari, name='koda_raporlari'),
    path('kurumsal-destek/', views.kurumsal_destek, name='kurumsal_destek'),
    path('koda-haritasi/', views.koda_haritasi, name='koda_haritasi'),
    path('cozum-masasi/', views.cozum_masasi, name='cozum_masasi'),
    path('etkinlik-onerileri/', views.etkinlik_onerileri, name='etkinlik_onerileri'),
    re_path(r'etkinlik-onerileri/(?P<id>[\w-]+)/$', views.etkinlik_onerileri_detay, name='etkinlik_onerileri_detay'),
    path('ogretmenlerden-gelen-etkinlikler/', views.ogretmenlerden_gelen_etkinlikler, name='ogretmenlerden_gelen_etkinlikler'),
    re_path(r'ogretmenlerden-gelen-etkinlikler/(?P<id>[\w-]+)/$', views.ogretmenlerden_gelen_etkinlikler_detay, name='ogretmenlerden_gelen_etkinlikler_detay'),
    path('onerilen-kaynaklar/', views.onerilen_kaynaklar, name='onerilen_kaynaklar'),
    re_path(r'onerilen-kaynaklar/(?P<id>[\w-]+)/$', views.onerilen_kaynaklar_detay,
            name='onerilen_kaynaklar_detay'),

    path('tipoti-galima-ve-pako/', views.tipoti_galima_ve_pako, name='tipoti_galima_ve_pako'),
    re_path(r'tipoti-galima-ve-pako/(?P<id>[\w-]+)/$', views.tipoti_galima_ve_pako_detay,
            name='tipoti_galima_ve_pako_detay'),
    path('koylerde-uzaktan-egitim-ve-covid19/', views.koylerde_uzaktan_egitim_ve_covid19, name='koylerde_uzaktan_egitim_ve_covid19'),
    re_path(r'koylerde-uzaktan-egitim-ve-covid19/(?P<id>[\w-]+)/$', views.koylerde_uzaktan_egitim_ve_covid19_detay,
            name='koylerde_uzaktan_egitim_ve_covid19_detay'),

    path('koda-gunceleri/', views.koda_gunceleri,
         name='koda_gunceleri'),
    re_path(r'koda-gunceleri/(?P<id>[\w-]+)/$', views.koda_gunceleri_detay,
            name='koda_gunceleri_detay'),

    path('il-milli-egitim-mudurlukleri/', views.il_milli_egitim,
             name='il_milli_egitim'),

    re_path(r'onerilen-siteler/(?P<id>[\w-]+)/$', views.onerilen_siteler_detay,
            name='onerilen_siteler_detay'),

    path('onerilen-siteler/', views.onerilen_siteler,
         name='onerilen_siteler'),
    path('covid-19-bilgi-iletisim-agi/', views.covid_bilgi_iletisim,
         name='covid_bilgi_iletisim'),
    path('bia-icerikler/', views.bia_icerikler,
         name='bia-icerikler'),
    path('renklerin-dansi/', views.renklerin_dansi,
         name='renklerin_dansi'),
    path('destekcilerimiz/', views.destekcilerimiz,
         name='destekcilerimiz'),
    path('ogretmenlere-tavsiyeler-ve-cevre-etkinlik-plani/', views.ogretmenlere_tavsiyeler_ve_cevre_etkinlik,
         name='ogretmenlere_tavsiyeler_ve_cevre_etkinlik'),

    path('kvkk-basvuru-formu/', views.kvkk_basvuru,
         name='kvkk_basvuru_formu'),
    path('kvkk-bilgilendirme-metni/', views.kvkk_info,
         name='kvkk_bilgilendirme_metni'),
    path('cerez-politikası/', views.cookies_policy,
         name='cerez_politikasi'),
    path('kullanım-kosullari-gizlilik/', views.kvkk_politics,
         name='kullanim_kosullari_gizlilik'),

]
