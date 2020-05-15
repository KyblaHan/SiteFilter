from django.db import models

# Create your models here.

class InputImage(models.Model):
    img = models.ImageField("Входное изображение")
    name = models.CharField("Название картинки", max_length=200)

    def __str__(self):
        return self.name



class OutputImage(models.Model):
    img = models.ImageField("Выходное изображение")
    name = models.CharField("Название картинки", max_length=200)
    sigma_color = models.IntegerField("SigmaColor")
    sigma_space = models.IntegerField("SigmaSpace")
    date = models.DateTimeField("Дата создания")

    def __str__(self):
        return self.name