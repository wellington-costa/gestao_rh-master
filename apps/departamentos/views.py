from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DeleteView

from .models import Departamento




class ListDepartamentos(ListView):
    model = Departamento
    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Departamento.objects.filter(empresa = empresa_logada)

class UpdateDepartamento(UpdateView):
    model = Departamento
    fields = ['nome']

class CreateDepartamento(CreateView):
    model = Departamento
    fields = ['nome']

    def form_valid(self, form):
        departamento = form.save(commit = False)
        departamento.empresa = self.request.user.funcionario.empresa
        departamento.save()
        return super(CreateDepartamento, self).form_valid(form)



class DeleteDepartamento(DeleteView):
    model = Departamento
    success_url = reverse_lazy('list_departamentos')