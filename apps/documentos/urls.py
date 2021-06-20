from django.urls import path
from .views import DocumentosList, DocumentoEdit, DocumentoDelete, DocumentoCreate


urlpatterns = [
    path('', DocumentosList.as_view(), name='list_documentos'),
    path('novo/', DocumentoCreate.as_view(), name='create_documento'),
    path('editar/<int:pk>/', DocumentoEdit.as_view(), name='update_documento'),
    path('deletar/<int:pk>/', DocumentoDelete.as_view(), name='delete_documento'),
]
