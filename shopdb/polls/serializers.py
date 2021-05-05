from rest_framework import serializers
from polls.models import Produkty


class ProduktySerializer(serializers.ModelSerializer):

    class Meta:
        model = Produkty
        fields = '__all__'