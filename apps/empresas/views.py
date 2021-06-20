from django.shortcuts import render
from django.views.generic import CreateView
from apps.empresas.models import Empresa


class EmpresaCreate(CreateView):
    model = Empresa
    fields = ['nome']
