from rest_framework import serializers
from safo_eshiklar.models import Contact


class CntSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
