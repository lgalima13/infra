from django.contrib import admin
from .models import Aniversariante

@admin.register(Aniversariante)
class AniversarianteAdmin(admin.ModelAdmin):
    list_display = ['nome', 'setor', 'local', 'datanascimento', 'status', 'foto']