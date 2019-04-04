from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum

from apps.departamentos.models import Departamento
from apps.empresa.models import Empresa
from django.urls import reverse

class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    usuario = models.OneToOneField(User, on_delete=models.PROTECT)
    departamento = models.ManyToManyField(Departamento)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT, null=True, blank=True)

    def get_absolute_url(self):
       return reverse('list_funcionarios')

    @property
    def total_hora_extra(self):
        total = self.registrohoraextra_set.all().aggregate(Sum('horas'))['horas__sum']
        return total


    def __str__(self):
        return self.nome
