# -*- coding: utf-8 -*-
from django.db import models

SEXO = (
		(u'masculino', u'Masculino'),
        (u'feminino', u'Feminino'),
	)

class Pessoa(models.Model):
	
	pessoa_id = models.AutoField(primary_key=True)
	pessoa_nome = models.CharField(max_length=45, verbose_name='Nome')
	pessoa_email = models.EmailField(max_length=255, blank=True, verbose_name='Email')
	pessoa_nascimento = models.DateField(verbose_name='Data de Nascimento')
	pessoa_sexo = models.CharField(max_length=10, choices=SEXO, verbose_name='Sexo')
	pessoa_foto = models.ImageField(max_length=255, blank=True, upload_to='pessoa/%Y', verbose_name='Foto')

	def __unicode__(self):
	    return self.pessoa_nome
	class Meta:
	    db_table = u'pessoa'
	    verbose_name = 'Pessoa'
	    verbose_name_plural = 'Pessoas'
	    ordering = ['pessoa_nome']
