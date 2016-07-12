# -*- coding: utf-8 -*-
from django import forms
from .models import Pessoa


class PessoaForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = Pessoa
        fields = ['pessoa_email', 'pessoa_nome', 'pessoa_senha']
        widgets = {
            'pessoa_email': forms.TextInput(attrs={'class': 'form-control'}),
            'pessoa_nome': forms.TextInput(attrs={'class': 'form-control'}),
            'pessoa_senha': forms.TextInput(attrs={'class': 'form-control'}),
        }
