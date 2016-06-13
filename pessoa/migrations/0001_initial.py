# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('pessoa_id', models.AutoField(serialize=False, primary_key=True)),
                ('pessoa_nome', models.CharField(max_length=45, verbose_name=b'Nome')),
                ('pessoa_email', models.EmailField(max_length=255, verbose_name=b'Email', blank=True)),
                ('pessoa_nascimento', models.DateField(verbose_name=b'Data de Nascimento')),
                ('pessoa_sexo', models.CharField(max_length=10, verbose_name=b'Sexo', choices=[(1, b'Masculino'), (2, b'Feminino')])),
                ('pessoa_foto', models.ImageField(upload_to=b'contato/%Y', max_length=255, verbose_name=b'Foto', blank=True)),
            ],
            options={
                'ordering': ['pessoa_nome'],
                'db_table': 'pessoa',
                'verbose_name': 'Pessoa',
                'verbose_name_plural': 'Pessoas',
            },
        ),
    ]
