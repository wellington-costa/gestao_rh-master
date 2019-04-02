from django.db import models
from django.urls import reverse
from django.utils.datetime_safe import date

from apps.funcionarios.models import Funcionario

class RegistroHoraExtra(models.Model):
    motivo = models.CharField(max_length=100)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.PROTECT)
    horas = models.DecimalField(max_digits=5, decimal_places=2)
    data_hora = models.DateField(auto_now_add=False, auto_now=False, default=date.today)


    def __str__(self):
        return self.motivo

    def get_absolute_url(self):
       return reverse('list_hora_extra')
