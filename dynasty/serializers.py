from rest_framework import serializers

from .models import Dynasty


class DynastySerializer(serializers.ModelSerializer):
    class Meta:
        model = Dynasty
        fields = ['name', 'begin_year', 'end_year']
