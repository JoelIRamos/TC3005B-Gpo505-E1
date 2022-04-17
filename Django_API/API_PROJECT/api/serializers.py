from rest_framework import serializers
from api.models import Table, History, File, LastSession

class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = ('TableID', 'TableName', 'TableNum')


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ('HistoryID', 'DateCreated', 'DateModified')


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ('FileID', 'HistoryID', 'Atribute')


class LastSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = LastSession
        fields = ('LastSessionID', 'HistoryID', 'WebUserID')