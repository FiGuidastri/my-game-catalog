from django.contrib import admin
from .models import Jogo, Avaliacao, TempoDeJogo, Tag

# Registro dos modelos para que apareçam no Django Admin
admin.site.register(Jogo)
admin.site.register(Avaliacao)
admin.site.register(TempoDeJogo)
admin.site.register(Tag)
