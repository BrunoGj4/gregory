from django.db import models
from empresas.models import Empresa
from django.shortcuts import reverse


class Departamento(models.Model):
   nome = models.CharField(max_length=70)
   empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)
   
   def get_absolute_url(self):
       return reverse("departamentos:lista_departamento")
   
   
   def __str__(self):
       return self.nome
   