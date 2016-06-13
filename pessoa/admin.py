# -*- coding: utf-8 -*-
from pessoa.models import Pessoa
from django.contrib import admin

class PessoaAdmin(admin.ModelAdmin):
    model = Pessoa
    list_display = ['pessoa_nome','pessoa_email']
    list_filter = ['pessoa_sexo']
    search_fields = ['pessoa_nome']
    save_on_top = True
admin.site.register(Pessoa, PessoaAdmin)