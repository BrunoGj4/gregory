from django.views.generic import ListView, UpdateView, DeleteView
from .models import Funcionario
from django.urls import reverse_lazy

class FuncionariosList(ListView):
   model = Funcionario
   
   def get_queryset(self):
      empresa_logada = self.request.user.funcionario.empresa
      
      return Funcionario.objects.filter(empresa=empresa_logada)
   
class FuncionariosEdit(UpdateView):
   model = Funcionario
   fields = ['nome', 'departamentos']
   

class FuncionariosDelete(DeleteView):
   model = Funcionario
   success_url = reverse_lazy('funcionarios:lista_funcionarios')