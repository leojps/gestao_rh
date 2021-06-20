from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('apps.core.urls')),
    path('funcionarios/', include('apps.funcionarios.urls')),
    path('departamentos/', include('apps.departamentos.urls')),
    path('registro_hora_extra/', include('apps.registro_hora_extra.urls')),
    path('documentos/', include('apps.documentos.urls')),
    path('empresa/', include('apps.empresas.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
]
