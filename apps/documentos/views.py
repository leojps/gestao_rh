from django.contrib.auth.models import User
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView

from .models import Documento


class DocumentosList(ListView):
    model = Documento

    def get_queryset(self):
        dono = self.request.user.funcionario
        return Documento.objects.filter(pertence=dono)


class DocumentoEdit(UpdateView):
    model = Documento
    fields = ['nome', 'pertence']
    success_url = reverse_lazy('list_documentoss')


class DocumentoDelete(DeleteView):
    model = Documento
    success_url = reverse_lazy('list_documentoss')


class DocumentoCreate(CreateView):
    model = Documento
    fields = ['nome', 'pertence']

    def form_valid(self, form):
        Doc = form.save(commit=False)
        Doc.pertence = self.request.user.funcionario
        Doc.save()
        return super(DocumentoCreate, self).form_valid(form)
