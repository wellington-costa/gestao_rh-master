import self as self
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Funcionario
from django.views.generic.list import ListView

class CreateFuncionario(CreateView):
     model = Funcionario
     fields = ['nome', 'departamento']

     def form_valid(self, form):
      funcionario = form.save(commit=False)
      funcionario.empresa = self.request.user.funcionario.empresa
      username = funcionario.nome.split(' ')[0] + funcionario.nome.split(' ')[1]
      funcionario.usuario = User.objects.create(username=username)
      funcionario.save()
      return super(CreateFuncionario, self).form_valid(form)


class ListFuncionarios(ListView):
     model = Funcionario

     def get_queryset(self):
          empresa_logada = self.request.user.funcionario.empresa
          queryset = Funcionario.objects.filter(empresa = empresa_logada)
          return queryset

class UpadteFuncionarios(UpdateView):
     model = Funcionario
     fields = ['nome', 'departamento']

class DeleteFuncionario(DeleteView):
     model = Funcionario
     success_url = reverse_lazy('list_funcionarios')



