# Generated by Django 3.1.3 on 2020-11-24 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='date_of_birth',
            field=models.DateField(null=True),
        ),
    ]
