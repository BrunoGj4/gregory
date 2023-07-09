from django.urls import path
from . import views

app_name = 'funcionarios'

urlpatterns = [
    path('', views.FuncionariosList.as_view(), name="lista_funcionarios")
]
