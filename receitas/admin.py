from django.contrib import admin
from receitas.models import Category, Receita


class CategoryAdmin(admin.ModelAdmin):
    ...

admin.site.register(Category, CategoryAdmin)