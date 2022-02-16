from django.forms import ModelForm
from .models import Invoice, MoreInfo, Score

class InvoiceForm(ModelForm):
    class Meta:
        model = Invoice
        fields = ['tytul', 'opis', 'premiera', 'rok', 'imdb_rating', 'plakat']


class MoreInfoForm(ModelForm):
    class Meta:
        model = MoreInfo
        fields = ['czas_trwania', 'gatunek']

class ScoreForm(ModelForm):
    class Meta:
        model = Score
        fields = ['gwiazdki', 'recenzja']
