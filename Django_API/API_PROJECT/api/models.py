from django.db import models

# Create your models here.

class Table(models.Model):
    TableID = models.AutoField(primary_key=True)
    TableName = models.CharField(max_length=500)