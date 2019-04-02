from django.urls import path
from .views import CreateDocumento

urlpatterns = [

    path('novo/<int:funcionario_id>/', CreateDocumento.as_view(), name = 'create_documento'),

]