from django.urls import path, include
from .views import CreateFuncionario, ListFuncionarios, UpadteFuncionarios, DeleteFuncionario

urlpatterns = (

    path('novo', CreateFuncionario.as_view(), name = 'create_funcionario'),
    path('', ListFuncionarios.as_view(), name = 'list_funcionarios'),
    path('editar/<int:pk>/', UpadteFuncionarios.as_view(), name = 'update_funcionario'),
    path('deletar/<int:pk>/', DeleteFuncionario.as_view(), name = 'delete_funcionario'),


)
