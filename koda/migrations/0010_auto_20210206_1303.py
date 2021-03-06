# Generated by Django 2.2.14 on 2021-02-06 13:03

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('koda', '0009_kodakvkkforms'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=250)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='kodateam',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='Ekibimiz'),
        ),
    ]
