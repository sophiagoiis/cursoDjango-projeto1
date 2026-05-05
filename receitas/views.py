from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#HTTP REQUEST
def home(request):
    return render(request, 'receitas/home.html', context={
        'name': 'Sophia Maria',
        'age': 19,
    })

