# Generated by Django 3.1.3 on 2021-01-06 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0003_auto_20210103_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mpesapayment',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='mpesapayment',
            name='middle_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='mpesapayment',
            name='payment_type',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='mpesapayment',
            name='reference',
            field=models.TextField(null=True),
        ),
    ]
