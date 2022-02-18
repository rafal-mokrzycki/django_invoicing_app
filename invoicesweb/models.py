import datetime
import re

from django.db import models
from django.utils import timezone, dateformat
from django.core.validators import RegexValidator
from django import forms
from django.core.validators import validate_email
from django.core import validators
from django.forms import CharField


class InvoiceNumber(models.CharField):

    def __init__(self, *args, **kwargs):
        kwargs['default'] = datetime.datetime.today().strftime('%Y/%m') + '/02'  # TODO: \
        # add method to calculate number of invoices
        kwargs['primary_key'] = True
        kwargs['max_length'] = 11
        super().__init__(*args, **kwargs)




class Invoice(models.Model):
    invoice_type = models.CharField(choices=[
        (0, 'Normal'),
        (1, 'Correction'),
        (2, 'Proforma'),
    ], default=0, null=False, blank=False, max_length=1)
    # dodatkowe = models.OneToOneField(DodatkoweInfo, on_delete=models.CASCADE, null=True, blank=True)
    invoice_number = InvoiceNumber()
    contractor_tax_number = models.CharField(
        max_length=30,
        blank=False,
        validators=[
            RegexValidator(
                regex='\d{10}|\d{11}',
                message='Tax number consists of 10 or 11 characters',
                code='invalid_tax_number'
            ),
        ]
    )
    issue_date = models.DateField(null=False,
                                  blank=False,
                                  default=datetime.datetime.today().strftime('%Y-%m-%d'))
    #invoice_position = InvoicePosition()


class InvoicePosition(models.Model):
    product_or_service = models.TextField(primary_key=True, default="flower")
    unit = models.CharField(choices=[
        (0, 'pcs.'),
        (1, 'serv.'),
        (2, 'm'),
        (3, 'l'),
        (4, 'kg'),
    ], default=0, null=False, blank=False, max_length=1)
    price_per_unit_net = models.DecimalField(null=False, blank=False, max_digits=8,
                                             decimal_places=2, default=0.00)
    amount = models.PositiveSmallIntegerField(null=False, blank=False, default=1)
    total_price_net = models.DecimalField(null=False, blank=False, max_digits=8,
                                          decimal_places=2, default=0.00)
    tax_rate = models.CharField(choices=[
        (0, .23),
        (1, .08),
        (2, .05),
        (3, .0),
        (4, 'free'),
    ], default=.23, null=False, blank=False, max_length=1)
    total_price_gross = models.DecimalField(null=False, blank=False, max_digits=8,
                                            decimal_places=2, default=0.00)
    # Invoice = models.ForeignKey("Invoice", on_delete=models.CASCADE)




class Contractor(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    company_name = models.CharField(max_length=32)
    tax_number = models.CharField(max_length=32, default='1')
    contractor_tax_number = models.CharField(
        max_length=30,
        blank=False,
        primary_key=True,
        default=9999999999,
        validators=[
            RegexValidator(
                regex='\d{10}|\d{11}',
                message='Tax number consists of 10 or 11 characters',
                code='invalid_tax_number'
            ),
        ]
    )
    street = models.CharField(max_length=32)
    house_number = models.SmallIntegerField()
    flat_number = models.SmallIntegerField(blank=True)
    email = models.EmailField(unique=True)
    phone_number = models.PositiveSmallIntegerField()
