from django.urls import path
from .views import Hora_extraList, Hora_extraEdit, Hora_extraDelete, Hora_extraCreate


urlpatterns = [
    path('', Hora_extraList.as_view(), name='list_registro_hora_extra'),
    path('novo/', Hora_extraCreate.as_view(), name='create_registro_hora_extra'),
    path('editar/<int:pk>/', Hora_extraEdit.as_view(), name='update_registro_hora_extra'),
    path('deletar/<int:pk>/', Hora_extraDelete.as_view(), name='delete_registro_hora_extra'),
]
