# Generated by Django 2.2.14 on 2021-01-31 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('koda', '0006_kvkkform'),
    ]

    operations = [
        migrations.CreateModel(
            name='KodaTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('title', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=250)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
