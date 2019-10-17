from django.db import models

# Create your models here.
class calGraphicData(models.Model):
    name = models.TextField()
    data = models.TextField(max_length=10)
    def __str__(self):
        return self.data