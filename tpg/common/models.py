from django.db import models

class Package(models.Model):
    name = models.CharField(max_length=200)
    status = models.IntegerField(default=0)
