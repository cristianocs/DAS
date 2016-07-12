# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

import logging
logr = logging.getLogger(__name__)

class Pessoa(models.Model):
	
	pessoa_id = models.AutoField(primary_key=True)
	pessoa_nome = models.CharField(max_length=45, verbose_name='Nome')
	pessoa_email = models.EmailField(max_length=255, blank=True, verbose_name='Email')
	pessoa_senha = models.CharField(max_length=50, verbose_name='Senha')

	def __unicode__(self):
	    return self.pessoa_nome
	class Meta:
	    db_table = u'pessoa'
	    verbose_name = 'Pessoa'
	    verbose_name_plural = 'Pessoas'
	    ordering = ['pessoa_nome']

User.profile = property(lambda u: Pessoa.objects.get_or_create(pessoa_id=u)[0])

@receiver(post_save, sender=User)
def user_added(sender, **kwargs):
	if kwargs.get('created', False):
		up = Pessoa.objects.create(pessoa_id=kwargs.get('instance'))
		logr.debug("Pessoa criada: %s" % up)