# from django.contrib.auth.models import User
# from rest_framework import serializers
# from .models import Invoice, Contractor
#
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ['username', 'email']
#
# class InvoiceSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Invoice
#         fields = ['invoice_type', 'invoice_number', 'contractor_tax_number', 'issue_date']#'__all__'#, 'invoice_position']
#
# class ContractorSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Contractor
#         fields = '__all__'#['first_name','last_name', 'company_name', 'street', 'house_number', 'flat_number', 'tax_number']
