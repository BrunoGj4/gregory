from django.db import models
from funcionarios.models import Funcionario
# Create your models here.
class RegistroHoraExtra(models.Model):
   motivo = models.CharField(max_length=100)
   colaborador = models.ForeignKey(Funcionario, on_delete=models.PROTECT, default="")
   def __str__(self):
       return self.motivo
   