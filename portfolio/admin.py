from django.contrib import admin

# Register your models here.
from .models import Cadeira, Pessoa, Projeto, Elogio, Competencia, PontuacaoQuizz, Noticia

admin.site.register(Cadeira)
admin.site.register(Pessoa)
admin.site.register(Projeto)
admin.site.register(Elogio)
admin.site.register(Competencia)
admin.site.register(PontuacaoQuizz)
admin.site.register(Noticia)
