# Generated by Django 3.1.3 on 2021-01-03 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_auto_20210103_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mpesapayment',
            name='organization_balance',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]
