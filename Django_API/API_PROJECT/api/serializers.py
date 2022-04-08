from rest_framework import serializers
from api.models import Table

class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = ('TableID', 'TableName')