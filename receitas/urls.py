from django.urls import path

from receitas import views

urlpatterns = [
    path('', views.home), #boto o nome do caminho e dps a função que vai ser chamada quando o usuário acessar esse caminho
    path('receitas/<int:id>/', views.receita),
]

