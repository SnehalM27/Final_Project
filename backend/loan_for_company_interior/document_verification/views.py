from django.shortcuts import render
from rest_framework import viewsets
from .serializers import BankSerializer , DocumentSerializer
from .models import Bank , Document

# Create your views here.
class BankViewSet(viewsets.ModelViewSet):
    serializer_class = BankSerializer
    queryset = Bank.objects.all()


class DocumentViewSet(viewsets.ModelViewSet):
    serializer_class = DocumentSerializer
    queryset = Document.objects.all()
    