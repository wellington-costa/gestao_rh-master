from django.urls import path
from .views import ListDepartamentos, CreateDepartamento, DeleteDepartamento, UpdateDepartamento

urlpatterns = (
    path('', ListDepartamentos.as_view(), name = 'list_departamentos'),
    path('novo', CreateDepartamento.as_view(), name = 'create_departamento'),
    path('deletar/<int:pk>', DeleteDepartamento.as_view(), name = 'delete_departamento'),
    path('update/<int:pk>', UpdateDepartamento.as_view(), name = 'update_departamento'),
)