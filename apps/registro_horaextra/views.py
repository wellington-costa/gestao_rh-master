from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DeleteView

from apps.registro_horaextra.forms import RegistroHoraExtraForm
from apps.registro_horaextra.models import RegistroHoraExtra


class ListHoraExtra(ListView):
    model = RegistroHoraExtra

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        queryset = RegistroHoraExtra.objects.filter(funcionario__empresa=empresa_logada)
        return queryset
class UpdateHoraExtra(UpdateView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm

    def get_form_kwargs(self):
        kwargs = super(UpdateHoraExtra, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs



class CreateHoraExtra(CreateView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm

    def get_form_kwargs(self):
        kwargs = super(CreateHoraExtra, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs





class DeleteHoraExtra(DeleteView):
    model = RegistroHoraExtra
    success_url = reverse_lazy('list_hora_extra')

