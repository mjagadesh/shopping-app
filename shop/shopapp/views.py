from django.shortcuts import render

from django.core import serializers
from rest_framework import viewsets
from .import models
from .import serializers

class ShoppingDetails(viewsets.ModelViewSet):
    queryset = models.Shop.objects.all()
    serializer_class = serializers.ShoppingSerializer