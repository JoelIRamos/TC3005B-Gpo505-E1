from django.db import models

# Create your models here.

class Table(models.Model):
    TableID = models.AutoField(primary_key=True)
    TableName = models.CharField(max_length=500)
    TableNum = models.IntegerField(default=0)

class History(models.Model):
    HistoryID = models.AutoField(primary_key=True)
    DateCreated = models.DateTimeField(auto_now_add=True)
    DateModified = models.DateTimeField(auto_now=True)

class File(models.Model):
    FileID = models.AutoField(primary_key=True)
    HistoryID = models.IntegerField()
    Atribute = models.TextField() # max_length=5000

class LastSession(models.Model):
    LastSessionID = models.AutoField(primary_key=True)
    HistoryID = models.IntegerField()
    WebUserID = models.IntegerField()
    # WebUserID = models.CharField(max_length=50)