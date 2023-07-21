from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .models import Documentos
from django.urls import reverse_lazy
from django.contrib.auth.models import User


class DocumentoCreate(CreateView):
   model = Documentos
   fields = ['descricao','arquivo']

   def post(self, request, *args, **kwargs):
      form = self.get_form()
      form.instance.pertence_id = self.kwargs['funcionario_id']

      if form.is_valid():
         return self.form_valid(form)
      else:
         return self.form_invalid(form)

   def get_success_url(self):
      return reverse('update_funcionarios', args=[self.kwargs['funcionario_id']])