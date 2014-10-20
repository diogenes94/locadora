from django.contrib import admin
from models import Filme 
from models import Pessoa
from models import Alugar
from models import Categoria
from models import subAluguel


class FilmesInline(admin.TabularInline):
	model = subAluguel
	extra = 1
# Register your models here.
class FilmeAdmin (admin.ModelAdmin):
	search_fields=['Nome_Filme']

class PessoaAdmin(admin.ModelAdmin):
	search_fields = ['Nome','CPF']

class AlugarAdmin(admin.ModelAdmin):
	inlines = [FilmesInline]

admin.site.register(Filme,FilmeAdmin)
admin.site.register(Pessoa,PessoaAdmin)
admin.site.register(Alugar,AlugarAdmin)
admin.site.register(Categoria)
#admin.site.register(subAluguel)
