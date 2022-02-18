from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Invoice, Contractor

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['issue_date','username', 'email']

class InvoiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Invoice
        fields = ['invoice_type', 'invoice_number', 'contractor_tax_number', 'issue_date']

class ContractorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contractor
        fields = ['first_name','last_name', 'company_name', 'street', 'house_number', 'flat_number', 'tax_number']
