import datetime

from django.db import models


class MoreInfo(models.Model):
    GATUNEK = {
        (0, 'Inne'),
        (1, 'Horror'),
        (2, 'Komedia'),
        (3, 'Sci-fi'),
        (4, 'Drama'),
    }

    czas_trwania = models.PositiveSmallIntegerField(default=0)
    gatunek = models.PositiveSmallIntegerField(default=0, choices=GATUNEK)


class Invoice(models.Model):
    # invoice_number = models.CharField(max_length=64, blank=False, unique=True)
    invoice_number = models.CharField(blank=False, max_length=12, primary_key=True)  # TODO: add a custom class
    contractor_tax_number = models.PositiveIntegerField(default=99999999999,
                                                        blank=False)  # TODO: add a custom class checcking for NIP or PESEL pattern
    opis = models.TextField(default="")
    issue_date = models.DateField(null=True, blank=False, default=datetime.datetime.today())
    imdb_rating = models.DecimalField(max_digits=4, decimal_places=2,
                                      null=True, blank=True)
    plakat = models.ImageField(upload_to="plakaty", null=True, blank=True)
    dodatkowe = models.OneToOneField(MoreInfo, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.tytul_z_contractor_tax_numberiem()

    def tytul_z_contractor_tax_numberiem(self):
        return "{} ({})".format(self.invoice_number, self.contractor_tax_number)


class Score(models.Model):
    recenzja = models.TextField(default="", blank=True)
    gwiazdki = models.PositiveSmallIntegerField(default=5)
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)


class Actor(models.Model):
    imie = models.CharField(max_length=32)
    nazwisko = models.CharField(max_length=32)
    invoices = models.ManyToManyField(Invoice, related_name="actors")


class Contractor(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    company_name = models.CharField(max_length=32)
    tax_number = models.PositiveIntegerField(default=99999999999,
                                             primary_key=True)  # TODO: add a custom class checcking for NIP or PESEL pattern
    street = models.CharField(max_length=32)
    house_number = models.SmallIntegerField()
    flat_number = models.SmallIntegerField(blank=True)
    email = models.EmailField()
    phone_number = models.PositiveSmallIntegerField()

