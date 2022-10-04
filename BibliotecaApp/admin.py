from django.contrib import admin
from .models import Livro

@admin.register(Livro)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','titulo','autor','descricao','genero','qntd_livro','data_lancamento')

