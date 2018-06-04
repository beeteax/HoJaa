from django.db import models

# Create your models here.
class RemoteInput(models.Model):
    Address=models.CharField(max_length=100)
    Unit=models.IntegerField()
    Bedrooms=models.IntegerField()
    FullBath=models.IntegerField()
    HalfBath=models.IntegerField()
    Email=models.CharField(max_length=100)

    def __str__(self):
        return self.Address

        