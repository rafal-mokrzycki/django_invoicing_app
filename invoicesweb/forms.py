from django.forms import ModelForm
from .models import Invoice, Contractor, MoreInfo, Score

class InvoiceForm(ModelForm):
    class Meta:
        model = Invoice
        fields = ['invoice_number', 'opis', 'issue_date', 'contractor_tax_number', 'imdb_rating', 'plakat']

class ContractorForm(ModelForm):
    class Meta:
        model = Contractor
        fields = ['first_name','last_name', 'company_name', 'street', 'house_number', 'flat_number', 'tax_number']

class MoreInfoForm(ModelForm):
    class Meta:
        model = MoreInfo
        fields = ['czas_trwania', 'gatunek']

class ScoreForm(ModelForm):
    class Meta:
        model = Score
        fields = ['gwiazdki', 'recenzja']
