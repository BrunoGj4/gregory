from django.db import models
from funcionarios.models import Funcionario
from django.shortcuts import reverse

class Documentos(models.Model):
   descricao = models.CharField(max_length=100)
   pertence = models.ForeignKey(Funcionario, on_delete=models.PROTECT)
   arquivo = models.FileField(upload_to='documentos')
   
   def get_absolute_url(self):
       return reverse('update_funcionario', args=[self.pertece.id])
   
   
   def __str__(self):
       return self.descricao
   