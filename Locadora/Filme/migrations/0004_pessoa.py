# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Filme', '0003_auto_20141020_1959'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Nome', models.CharField(max_length=100, null=True, verbose_name=b'Nome')),
                ('Sexo', models.CharField(max_length=1, null=True, verbose_name=b'Sexo', choices=[(b'M', b'Masculino'), (b'F', b'Feminino')])),
                ('CPF', models.CharField(max_length=14, null=True, verbose_name=b'CPF')),
                ('DataNascimento', models.DateField(null=True, verbose_name=b'Data de Nascimento')),
                ('Telefone', models.CharField(max_length=15, null=True, verbose_name=b'Telefone')),
                ('Celular', models.CharField(max_length=15, null=True, verbose_name=b'Celular')),
                ('Email', models.EmailField(max_length=100, verbose_name=b'Endere\xc3\xa7o de email')),
                ('Logradouro', models.CharField(max_length=100, null=True, verbose_name=b'Logradouro')),
                ('Numero', models.IntegerField(null=True, verbose_name=b'N\xc3\xbamero')),
                ('Complemento', models.CharField(max_length=100, null=True, verbose_name=b'Complemento', blank=True)),
                ('Bairro', models.CharField(max_length=100, null=True, verbose_name=b'Bairro')),
                ('Cidade', models.CharField(max_length=100, null=True, verbose_name=b'Cidade')),
                ('Estado', models.CharField(max_length=2, null=True, verbose_name=b'UF')),
                ('CEP', models.CharField(max_length=9, null=True, verbose_name=b'CEP')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
