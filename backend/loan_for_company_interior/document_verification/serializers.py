from rest_framework import serializers
from .models import Bank, Document

class BankSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bank
        fields = '__all__'
        


class  DocumentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Document
        fields = '__all__'
