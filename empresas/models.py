from django.db import models
from django.shortcuts import reverse
# Create your models here.
class Empresa(models.Model):
   nome = models.CharField(max_length=100, help_text='Nome da empresa')
   
   def __str__(self):
       return self.nome
   
   def get_absolute_url(self):
       return reverse("core:home")
   