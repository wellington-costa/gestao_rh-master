from django.urls import path
from .views import EmpresaCreate, EmpresaUpdadte

urlpatterns = (
    path('novo', EmpresaCreate.as_view() , name = 'create_empresa'),
    path('editar/<int:pk>', EmpresaUpdadte.as_view() , name = 'update_empresa'),

)
