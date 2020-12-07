from django.db import models


class Traxxas(models.Model):
    title = models.CharField(max_length=30)
    category = models.CharField(max_length=20)
    image = models.ImageField(upload_to='pics',)
    description = models.TextField()
