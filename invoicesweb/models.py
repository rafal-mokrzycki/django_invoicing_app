import datetime
import re

from django.db import models
from django.utils import timezone, dateformat
from django.core.validators import RegexValidator
from django import forms
from django.core.validators import validate_email
from django.core import validators
from django.forms import CharField



class Invoice(models.Model):
    invoice_number = models.CharField(max_length=32, default=1)
    contractor_tax_number = models.CharField(
        max_length=30,
        blank=False,
        validators=[
            RegexValidator(
                regex='^[a-zA-Z0-9]*$',
                message='Username must be Alphanumeric',
                code='invalid_username'
            ),
        ]
    )  # TODO: add a custom class checking for NIP or PESEL pattern
    issue_date = models.DateField(null=False,
                                  blank=False,
                                  default=datetime.datetime.today().strftime('%Y-%m-%d'))



class Contractor(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    company_name = models.CharField(max_length=32)
    tax_number = models.PositiveIntegerField(default=99999999999,
                                             primary_key=True,
                                             unique=True)  # TODO: add a custom class checking for NIP or PESEL pattern
    street = models.CharField(max_length=32)
    house_number = models.SmallIntegerField()
    flat_number = models.SmallIntegerField(blank=True)
    email = models.EmailField(unique=True)
    phone_number = models.PositiveSmallIntegerField()
