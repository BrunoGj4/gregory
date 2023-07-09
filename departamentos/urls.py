from django.urls import path
from . import views

app_name = 'departamentos'

urlpatterns = [
    path('listar/', views.DepartamentoList.as_view(), name="lista_departamento"),
    path('criar/', views.DepartamentoNovo.as_view(), name="create_departamento"),
    path('editar/<int:pk>', views.DepartamentoEdit.as_view(), name="update_departamento"),
    path('deletar/<int:pk>', views.DepartamentoDelete.as_view(), name="delete_departamento"),
]
