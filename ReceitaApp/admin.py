from django.contrib import admin
from django.utils.html import mark_safe

from ReceitaApp.models import Categoria
from ReceitaApp.models import Receita

class ReceitaAdmin(admin.ModelAdmin):
    list_display=['Nome','Ingredientes','Modo_de_Preparo','Grau_de_Dificuldade']
    list_display_links=['Nome','Ingredientes']
    list_filter =['Nome','Grau_de_Dificuldade']

class CategoriaAdmin(admin.ModelAdmin):
    list_display=['Nome']
    list_display_links=['Nome']
    list_filter =['Nome']

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Receita, ReceitaAdmin)
# Register your models here.
