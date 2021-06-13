# Generated by Django 3.2.4 on 2021-06-13 12:10

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('koda', '0020_stratejikplanvemalibelgeler_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='BagisKartlari',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='bagis')),
                ('url', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='yayinlarimiz',
            name='image',
            field=models.ImageField(upload_to='yayinlarimiz/'),
        ),
    ]
