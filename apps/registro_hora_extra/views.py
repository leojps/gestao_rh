from django.contrib.auth.models import User
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView

from .models import RegistroHoraExtra


class Hora_extraList(ListView):
    model = RegistroHoraExtra

    def get_queryset(self):
        funcionario = self.request.user.funcionario
        return RegistroHoraExtra.objects.filter(funcionario=funcionario)


class Hora_extraEdit(UpdateView):
    model = RegistroHoraExtra
    fields = ['motivo']
    success_url = reverse_lazy('list_registro_hora_extra')


class Hora_extraDelete(DeleteView):
    model = RegistroHoraExtra
    success_url = reverse_lazy('list_registro_hora_extra')


class Hora_extraCreate(CreateView):
    model = RegistroHoraExtra
    fields = ['motivo']
    success_url = reverse_lazy('list_registro_hora_extra')

    def form_valid(self, form):
        horaextra = form.save(commit=False)
        horaextra.funcionario = self.request.user.funcionario
        horaextra.save()
        return super(Hora_extraCreate, self).form_valid(form)
