from django.db import models
from django.contrib.auth.models import User
from departamentos.models import Departamento
from empresas.models import Empresa
from django.shortcuts import reverse

class Funcionario(models.Model):
    nome = models.CharField(max_length=100) 
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    # user = models.ManyToManyField(Empresa)
    departamentos = models.ManyToManyField(Departamento)
    empresa = models.ForeignKey(
       Empresa, 
       on_delete=models.PROTECT,
       default="",
        null=True,
        blank=True,
    )
    
    def __str__(self):
        return self.nome
   
    def get_absolute_url(self):
       return reverse("funcionarios:lista_funcionarios")
   