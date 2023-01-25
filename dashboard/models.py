from django.db import models


class Datchiklar(models.Model):
    name = models.CharField(max_length=25)
