# Generated by Django 3.1.3 on 2020-12-24 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20201129_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='role',
            field=models.CharField(choices=[('admin', 'admin'), ('trainer', 'trainer'), ('player', 'player')], default='admin', max_length=30),
        ),
    ]
