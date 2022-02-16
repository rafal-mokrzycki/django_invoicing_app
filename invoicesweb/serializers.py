from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Invoice

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id','username', 'email']

class InvoiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Invoice
        fields = ['id','tytul','rok', 'opis', 'premiera']
