from django.db import models

# Create your models here.
class Quiz(models.Model):
    name=models.CharField(blank=True, null=True, verbose_name="問題名",max_length=10)
    text=models.TextField(blank=True, null=True, verbose_name="本文")
    answer=models.CharField(blank=True, null=True, verbose_name="答え",max_length=10)
