# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .form import ContactForm,GonulluForm,RuzgarGuluForm
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.shortcuts import render,redirect
from django.conf import settings
from django.views.decorators.cache import cache_page
from .models import EventSuggestions, SuggestedSources, TgpAdvantures
from django.shortcuts import render
from django.shortcuts import get_object_or_404


@cache_page(600 * 600)
def index(request):
    return render(request,'index.html')

def contact(request):
    my_form = ContactForm()
    context = {
        "form": my_form
    }
    if request.method == "POST":
        my_form = ContactForm(request.POST)
        if my_form.is_valid():
            print(my_form.cleaned_data)
        else:
            print(my_form.errors)

        msg_plain = render_to_string('email.txt', {'name': request.POST['name'], 'email': request.POST['email'],'content': request.POST['content'], 'phone': request.POST['phone']})
        msg_html = render_to_string('email.html', {'name': request.POST['name'], 'email': request.POST['email'],'content': request.POST['content'], 'phone': request.POST['phone']})
        message = '<p><strong>' + request.POST['name'] + '</strong> send you a message:' + request.POST['content'] + ' contact with email:' + request.POST['email'] + ' and phone. ' + request.POST['phone'] + '</p> '
        send_mail("Contact mail from More-Cow ",
                  message,
                  settings.EMAIL_HOST_USER,
                  ["menekse.cntn@gmail.com"],
                  html_message=msg_html,
                  fail_silently=False
                  )
    return render(request,'contact.html',context)


def about(request):
    return render(request,'about.html')

def galeri(request):
    return render(request,'galeri.html')

def index2(request):
    return render(request,'index2.html')

def basvuru(request):
    return render(request,'basvuru.html')

def bagis(request):
    return render(request,'bagis.html')


def gonullu(request):
    my_form = GonulluForm()
    context = {
        "form": my_form
    }
    if request.method == "POST":
        my_form = GonulluForm(request.POST)
        if my_form.is_valid():
            my_form.save()
            print(my_form.cleaned_data)
        else:
            print(my_form.errors)

        msg_plain = render_to_string('email.txt', {'name': request.POST['name'], 'email': request.POST['email'],'volunteer_type': request.POST['volunteer_type'], 'department': request.POST['department'], 'ruzgargulu': request.POST['ruzgargulu'],
                                                   'job': request.POST['job'], 'volunteer_preferences': request.POST['volunteer_preferences'], 'about_you': request.POST['about_you'],'workshop_accessories': request.POST['workshop_accessories'],
                                                   'volunteer_before': request.POST['volunteer_before'],'anything': request.POST['anything'], 'volunteer_content': request.POST['volunteer_content'],'cv': request.POST['cv']})
        msg_html = render_to_string('gonullu_basvuru.html', {'name': request.POST['name'], 'email': request.POST['email'],'volunteer_type': request.POST['volunteer_type'], 'department': request.POST['department'], 'ruzgargulu': request.POST['ruzgargulu'],
                                                   'job': request.POST['job'], 'volunteer_preferences': request.POST['volunteer_preferences'], 'about_you': request.POST['about_you'],'workshop_accessories': request.POST['workshop_accessories'],
                                                   'volunteer_before': request.POST['volunteer_before'],'anything': request.POST['anything'], 'volunteer_content': request.POST['volunteer_content'],'cv': request.POST['cv']})
        message = 'isim :'+ request.POST['name'] + 'telefon' +request.POST['phone'] + 'email' +request.POST['email']+  'Mesleğiniz:' +request.POST['job'] +'Mezun olduğunuz bölüm  :' + request.POST['department'] +'Daha önce gönüllü bir çalışmada yer aldınız mı? Evet ise kısaca bahseder misiniz?'+ request.POST['volunteer_before']+'Gönüllü eğitmenlik yapmanın sizin için önemi nedir? '+ request.POST['volunteer_content']+'Gerçekleştirmek istediğiniz atölye/eğitimin detayını paylaşır mısınız?:'+ request.POST['volunteer_type']+'Bu atölyeyi/eğitimi daha önce uyguladınız mı? Nerelerde ve hangi sıklıkta? Referans paylaşabilir misiniz?  :' + request.POST['volunteer_type_before']+'Atölye/eğitim süresi '+ request.POST['volunteer_type_content']+'Saha ziyareti yapmayı tercih eder misiniz yoksa sadece İstanbuldaki organizasyonlarda mı yer almak istersiniz?'+ request.POST['volunteer_preferences']+'Atölye/eğitim uygulayıcısı olarak sizi tanıtıcı kısa bir metin paylaşabilir misiniz? (Kısa özgeçmiş formatında):'+ request.POST['about_you']+'Atölyeyi uygulamak için malzeme gereksiniminiz bulunuyor mu? Malzemeleri siz tedarik edebilir misiniz?'+ request.POST['workshop_accessories']+'İletmek istediğiniz farklı bir detay bulunuyor mu?:'+request.POST['email']+'ruzgargulu katilim:'+request.POST['ruzgargulu']

        send_mail("Gonullu başvuru formu ",
                  message,
                  settings.EMAIL_HOST_USER,
                  ["ardasoylu39@hotmail.com"],
                  html_message=msg_html,
                  fail_silently=False
                  )
    return render(request,'gonullu.html',context)

def koy_ogretmenleri(request):
    return render(request,'koy_ogretmenleri_prj.html')

def mentorluk_programi(request):
    return render(request,'mentorluk_programi.html')

def gecmis_faaliyetler(request):
    return render(request,'gecmis_faaliyetler.html')

def ogretmen_topluluklari(request):
    return render(request,'ogretmen_topluluklari.html')


def bsmg_programi(request):
    return render(request,'bsmg_programi.html')


def cocuk_atolyeleri(request):
    return render(request,'cocuk_atolyeleri.html')

def degerlerimiz(request):
    return render(request,'degerlerimiz.html')

def ruzgargulubultenleri(request):
    my_form = RuzgarGuluForm()
    context = {
        "form": my_form
    }
    if request.method == "POST":
        my_form = GonulluForm(request.POST)
        if my_form.is_valid():
            my_form.save()
            print(my_form.cleaned_data)
        else:
            print(my_form.errors)

        msg_plain = render_to_string('email.txt', {'name': request.POST['name'], 'email': request.POST['email']})
        msg_html = render_to_string('gonullu_basvuru.html',
                                    {'name': request.POST['name'], 'email': request.POST['email']})
        message = 'isim :' + request.POST['name'] + 'email' + request.POST['email']
        send_mail("Rüzgar Gülü Haber Bülteni Takipçi ",
                  message,
                  settings.EMAIL_HOST_USER,
                  ["ardasoylu39@hotmail.com"],
                  html_message=msg_html,
                  fail_silently=False
                  )
    return render(request,'ruzgar_gulu_haber_bultenleri.html',context)


def products(request):
    return render(request,'products.html')

def sponsor(request):
    return render(request,'sponsor_olmak_istiyorum.html')

def isbirligi(request):
    return render(request,'koda_ile_isbirligi.html')

def bagis_detay(request):
    return render(request,'bagis_detay.html')

def neler_yapmiyoruz(request):
    return render(request,'neler_yapmiyoruz.html')

def yayinlarimiz(request):
    return render(request,'yayinlarimiz.html')

def bize_katilin(request):
    return render(request,'bize_katilin.html')

def koda_raporlari(request):
    return render(request,'koda_raporlari.html')

def koda_haritasi(request):

    return render(request,'koda_haritasi.html')

def kurumsal_destek(request):
    return render(request,'kurumsal_destek_ve_isbirligi.html')


def koda_gonullusu(request):
    return render(request,'koda_gonullusu.html')


def team(request):
    return render(request,'team.html')


def faaliyet_raporlari(request):
    return render(request,'faaliyet_raporlari.html')


def stratejimiz(request):
    return render(request,'stratejimiz.html')


def cozum_masasi(request):
    return render(request,'cozum_masasi.html')

def etkinlik_onerileri(request):
    context = EventSuggestions.objects.all()
    return render(request,'etkinlik_onerileri.html', {'context': context})

def etkinlik_onerileri_detay(request, id):
    context = get_object_or_404(EventSuggestions, pk=id)
    return render(request,'etkinlik_onerileri_detay.html', {'context': context})

def ogretmenlerden_gelen_etkinlikler(request):
    context = TeachersDocuments.objects.all()
    return render(request,'ogretmenlerden_gelen_etkinlikler.html', {'context': context})

def ogretmenlerden_gelen_etkinlikler_detay(request, id):
    context = get_object_or_404(TeachersDocuments, pk=id)
    return render(request,'ogretmenlerden_gelen_etkinlikler_detay.html', {'context': context})

def onerilen_kaynaklar(request):
    context = SuggestedSources.objects.all()
    return render(request,'onerilen_kaynaklar.html', {'context': context})

def onerilen_kaynaklar_detay(request, id):
    context = get_object_or_404(SuggestedSources, pk=id)
    return render(request,'onerilen_kaynaklar_detay.html', {'context': context})

def tipoti_galima_ve_pako(request):
    context = TgpAdvantures.objects.all()
    return render(request,'tipoti_galima_ve_pako.html', {'context': context})

def tipoti_galima_ve_pako_detay(request, id):
    context = get_object_or_404(TgpAdvantures, pk=id)
    return render(request,'tipoti_galima_ve_pako_detay.html', {'context': context})

def koylerde_uzaktan_egitim_ve_covid19(request):
    context = RemoteLearning.objects.all()
    return render(request,'koylerde_uzaktan_egitim_ve_covid19.html', {'context': context})

def koylerde_uzaktan_egitim_ve_covid19_detay(request):
    context = get_object_or_404(RemoteLearning, pk=id)
    return render(request,'koylerde_uzaktan_egitim_ve_covid19_detay.html', {'context': context})

