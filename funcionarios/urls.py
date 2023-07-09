from django.urls import path
from . import views

app_name = 'funcionarios'

urlpatterns = [
    path('', views.FuncionariosList.as_view(), name="lista_funcionarios"),
    path('novo/', views.FuncionariosNovo.as_view(), name="create_funcionarios"),
    path('editar/<int:pk>', views.FuncionariosEdit.as_view(), name="update_funcionarios"),
    path('deletar/<int:pk>', views.FuncionariosDelete.as_view(), name="delete_funcionarios"),
]
