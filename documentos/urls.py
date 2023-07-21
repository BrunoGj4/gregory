from django.urls import path
from . import views

app_name = 'documentos'

urlpatterns = [
    path('novo/',
         views.DocumentoCreate.as_view(), 
         name="create_documento"),
    
]
