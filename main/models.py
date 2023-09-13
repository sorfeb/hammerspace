from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()

    nama = models.CharField(max_length = 255, null=True)
    kelas = models.CharField(max_length = 255, null=True)
    aplikasi = models.CharField(max_length = 255, null=True)