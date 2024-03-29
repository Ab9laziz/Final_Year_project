# Generated by Django 3.1.3 on 2020-12-27 12:41

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('portal', '0006_auto_20201221_0950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainingsession',
            name='trainers',
            field=models.ManyToManyField(limit_choices_to={'role': 'trainer'}, related_name='training_sessions_assigned', to=settings.AUTH_USER_MODEL),
        ),
    ]
