from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()

class Personal(models.Model):
    nama = models.CharField(max_length = 255, null=True)
    kelas = models.CharField(max_length = 255, null=True)
    aplikasi = models.CharField(max_length = 255, null=True)