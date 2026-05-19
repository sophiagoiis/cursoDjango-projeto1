from django.urls import path

from receitas import views

#receitas:receita
app_name = 'receitas'

urlpatterns = [
    path('', views.home, name = "receitas-home"), #boto o nome do caminho e dps a função que vai ser chamada quando o usuário acessar esse caminho
    path('receitas/<int:id>/', views.receita, name = "receitas-receita"),
]

