from django.db import models
class Shops(models.Model):
    name=models.CharField(max_length=50)
    price=models.CharField(max_length=30)
    image=models.TextField(max_length=500)
   
    def __str__(self):
        return self.name