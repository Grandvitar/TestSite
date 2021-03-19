from django.db import models

class SaveModel(models.Model):
    image = models.ImageField(upload_to='images')
    name = models.CharField(max_length=20)




