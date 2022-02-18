from django.forms import ModelForm
from .models import Invoice, Contractor


class InvoiceForm(ModelForm):
    class Meta:
        model = Invoice
        fields = ['invoice_number', 'contractor_tax_number', 'issue_date']

class ContractorForm(ModelForm):
    class Meta:
        model = Contractor
        fields = ['first_name','last_name', 'company_name', 'street', 'house_number', 'flat_number', 'tax_number']
