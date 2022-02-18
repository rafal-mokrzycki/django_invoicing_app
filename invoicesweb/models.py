import datetime

from django.db import models
from django.utils import timezone, dateformat


class InvoiceNumber2(models.Field):
    description = "An invoice number following the pattern: YYYY/MM/number"

    def __init__(self, separator="/", year=datetime.datetime.year, month=datetime.datetime.month, *args, **kwargs):
        self.separator = separator,
        self.year = year
        self.month = month
        kwargs['unique'] = True
        super().__init__(*args, **kwargs)


class HandField(models.Field):

    def __init__(self, *args, **kwargs):

        kwargs['default'] = datetime.datetime.today().strftime('%Y/%m')
        kwargs['primary_key'] = True
        super().__init__(*args, **kwargs)

    # def deconstruct(self):
    #     name, path, args, kwargs = super().deconstruct()
    #     del kwargs["primary_key"]
    #     return name, path, args, kwargs



class Invoice(models.Model):
    invoice_number = HandField()
    # invoice_number = models.CharField(blank=False,
    #                                   max_length=12,
    #                                   primary_key=True,
    #                                   unique=True)  # TODO: add a custom class
    contractor_tax_number = models.PositiveIntegerField(default=99999999999,
                                                        blank=False)  # TODO: add a custom class checking for NIP or PESEL pattern
    issue_date = models.DateField(null=True,
                                  blank=False,
                                  default=dateformat.format(timezone.now(), 'Y-m-d'))

    def __str__(self):
        return self.tytul_z_contractor_tax_numberiem()

    def tytul_z_contractor_tax_numberiem(self):
        return "{} ({})".format(self.invoice_number, self.contractor_tax_number)


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
