from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()

    # def __str__(self):
    #     return self.name

    # def plus_item(self):
    #     # Increment the 'amount' field by 1 and save the object
    #     self.amount += 1
    #     self.save()

    # def minus_item(self):
    # # Decrement the 'amount' field by 1 if it's greater than 0 and save the object
    #     if self.amount > 0:
    #         self.amount -= 1
    #         self.save()

    # def delete_item(self):
    # # Delete the item from the database
    #     self.delete()

class Personal(models.Model):
    nama = models.CharField(max_length = 255, null=True)
    kelas = models.CharField(max_length = 255, null=True)
    aplikasi = models.CharField(max_length = 255, null=True)
