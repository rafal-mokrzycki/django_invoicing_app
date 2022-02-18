# Generated by Django 4.0.2 on 2022-02-18 18:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoicesweb', '0002_invoice_contractor_tax_number_invoice_invoice_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='contractor_tax_number',
            field=models.CharField(max_length=30, validators=[django.core.validators.RegexValidator(code='invalid_username', message='Username must be Alphanumeric', regex='^[a-zA-Z0-9]*$')]),
        ),
    ]
