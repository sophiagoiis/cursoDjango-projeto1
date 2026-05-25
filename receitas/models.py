from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=65)

    def __str__ (self):
        return self.name

class Receita(models.Model):
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=165)
    slug = models.SlugField
    preparation_time = models.IntegerField()
    preparation_time_unit = models.CharField(max_length=65)
    servings = models.IntegerField
    servings_unit = models.CharField(max_length=65)
    preparation_steps = models.TextField()
    preparation_steps_is_html = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='receitas/covers/%D/%m/%y/')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True )

    #CharField -> Campo de texto pequeno
    #TextField -> Texto grande
    #SlugField -> Texto para url
    #IntegerField -> Número inteiro
    #DateTimeField(auto_now_add=True) ->. No momento da criação ele gera uma data, poe la e nao mexe mais
    #BooleanField -> guarda True ou False
    #ImageField -> salva o caminho da imagem no banco e o upload_to Define a pasta onde a imagem será salva.
    #DateTimeField -> guarda data e horário