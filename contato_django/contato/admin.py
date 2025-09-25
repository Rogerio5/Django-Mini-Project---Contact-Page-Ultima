from django.contrib import admin
from .models import Mensagem

@admin.register(Mensagem)
class MensagemAdmin(admin.ModelAdmin):
    list_display = ("nome", "email", "criado_em")
    search_fields = ("nome", "email")


# Register your models here.
