from django.contrib import admin
from .models import Residente, Evento, responsavel, endereco, categoria, inscricao, feedback, Atividade, Administrador

class AtividadeInline(admin.TabularInline):
    model = Atividade
    extra = 1

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    inlines = [AtividadeInline]
    list_display = ('nome', 'descricao')

@admin.register(Administrador)
class AdministradorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo')

@admin.register(Atividade)
class AtividadeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')

@admin.register(Residente)
class residenteAdmin(admin.ModelAdmin):
    list_filter = ('data_nascimento',)
@admin.register(responsavel)
class ResponsavelAdmin(admin.ModelAdmin):
    list_display = ('telefone', 'celular', 'telefone_comercial')
    search_fields = ('telefone', 'celular', 'telefone_comercial')
@admin.register(endereco)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = ('logradouro', 'numero', 'bairro', 'cidade', 'estado', 'cep')
    search_fields = ('logradouro', 'bairro', 'cidade', 'estado', 'cep')


admin.site.register(categoria)
admin.site.register(inscricao)
admin.site.register(feedback)
