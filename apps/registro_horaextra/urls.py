from django.urls import path

from apps.registro_horaextra.views import ListHoraExtra, UpdateHoraExtra, CreateHoraExtra, DeleteHoraExtra, ListHoraExtraFuncionario


urlpatterns = [

    path('', ListHoraExtra.as_view(), name = 'list_hora_extra'),
    path('listagem/<int:funcionario_id>/', ListHoraExtraFuncionario.as_view(), name = 'list_hora_extra_func'),
    path('update/<int:pk>/', UpdateHoraExtra.as_view(), name = 'update_hora_extra'),
    path('novo', CreateHoraExtra.as_view(), name = 'create_hora_extra'),
    path('deletar/<int:pk>/', DeleteHoraExtra.as_view(), name = 'delete_hora_extra'),
]

