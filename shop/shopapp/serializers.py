from shopapp import models
from rest_framework import serializers

class ShoppingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Shop
        fields ='__all__'
        