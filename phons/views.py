from django.shortcuts import render
from rest_framework import generics

from .models import Phons
from .serializer import PhonsSerializer

class PhonsList(generics.ListAPIView):
    queryset = Phons.objects.all()
    serializer_class = PhonsSerializer

class PhonDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Phons.objects.all()
    serializer_class = PhonsSerializer
