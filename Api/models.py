from django.db import models

# Create your models here.
class RemoteInput(models.Model):
    TimeStamp=models.CharField(max_length=100)
    Text=models.CharField(max_length=1000)

    def __str__(self):
        return self.Text

        