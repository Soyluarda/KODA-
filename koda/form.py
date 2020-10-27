from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}),label="Ad-Soyad")
    email = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}),label="E-mail")
    phone = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}),label="Telefon")
    content = forms.CharField(widget=forms.Textarea(attrs={'class' : 'form-control'}),label="Mesaj")


class GonulluForm(forms.Form):
    CHOICES = [('1', 'Evet'), ('2', 'Hayır')]
    name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
    email = forms.CharField(label='Telefon numaranız',widget=forms.TextInput(attrs={'class' : 'form-control'}))
    phone = forms.CharField(label='Mail adresiniz ',widget=forms.TextInput(attrs={'class' : 'form-control'}))
    job = forms.CharField(label='Mesleğiniz',widget=forms.TextInput(attrs={'class' : 'form-control'}))
    department = forms.CharField(label='Mezun olduğunuz bölüm',widget=forms.TextInput(attrs={'class' : 'form-control'}))
    volunteer_before = forms.CharField(label='Daha önce gönüllü bir çalışmada yer aldınız mı? Evet ise kısaca bahseder misiniz?',widget=forms.Textarea(attrs={'class' : 'form-control'}))
    volunteer_content = forms.CharField(label='Gönüllü eğitmenlik yapmanın sizin için önemi nedir?',widget=forms.Textarea(attrs={'class' : 'form-control'}))
    volunteer_type =  forms.CharField(label='Gerçekleştirmek istediğiniz atölye/eğitimin detayını paylaşır mısınız?',widget=forms.Textarea(attrs={'class' : 'form-control'}))
    volunteer_type_before = forms.CharField(label='Bu atölyeyi/eğitimi daha önce uyguladınız mı? Nerelerde ve hangi sıklıkta? Referans paylaşabilir misiniz?',widget=forms.Textarea(attrs={'class' : 'form-control'}))
    volunteer_type_content = forms.CharField(label='Atölye/eğitim süresi',widget=forms.TextInput(attrs={'class' : 'form-control'}))
    volunteer_preferences = forms.CharField(label='Saha ziyareti yapmayı tercih eder misiniz yoksa sadece İstanbuldaki organizasyonlarda mı yer almak istersiniz?',widget=forms.Textarea(attrs={'class' : 'form-control'}))
    about_you = forms.CharField(label='Atölye/eğitim uygulayıcısı olarak sizi tanıtıcı kısa bir metin paylaşabilir misiniz? (Kısa özgeçmiş formatında) ',widget=forms.Textarea(attrs={'class' : 'form-control'}))
    workshop_accessories = forms.CharField(label='Atölyeyi uygulamak için malzeme gereksiniminiz bulunuyor mu? Malzemeleri siz tedarik edebilir misiniz? ',widget=forms.TextInput(attrs={'class' : 'form-control'}))
    anything = forms.CharField(label='İletmek istediğiniz farklı bir detay bulunuyor mu?',widget=forms.Textarea(attrs={'class' : 'form-control'}))
    ruzgargulu = forms.ChoiceField(label='Aylık yayınladığımız Rüzgar Gülü haber bülteninin mail ile sana ulaşmasını ister misin?',widget=forms.RadioSelect, choices=CHOICES)
    cv = forms.FileField()


class RuzgarGuluForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
