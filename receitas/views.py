from django.shortcuts import render
from django.http import HttpResponse
from utils.receitas.factory import make_receitas

# Create your views here.

#HTTP REQUEST
def home(request):
    return render(request, 'receitas/pages/home.html', context={
        'receitas': [make_receitas() for _ in range(10)],
    })

def receita(request, id):
    return render(request, 'receitas/pages/receitas-view', context={
        'recipe': make_receitas(),
    })


