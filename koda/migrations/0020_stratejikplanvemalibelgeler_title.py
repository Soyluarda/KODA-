# Generated by Django 2.2.14 on 2021-02-24 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('koda', '0019_stratejikplanvemalibelgeler_yayinlarimiz'),
    ]

    operations = [
        migrations.AddField(
            model_name='stratejikplanvemalibelgeler',
            name='title',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
