# Generated by Django 3.1.3 on 2020-12-17 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consentform',
            name='document',
            field=models.FileField(upload_to='consent-form/'),
        ),
    ]
