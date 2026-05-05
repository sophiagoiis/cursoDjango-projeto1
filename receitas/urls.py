from django.urls import path
from receitas.views import home

urlpatterns = [
    path('', home), #boto o nome do caminho e dps a função que vai ser chamada quando o usuário acessar esse caminho
]