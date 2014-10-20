# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Filme', '0004_pessoa'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aluga',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('DataEntrega', models.DateField(null=True, verbose_name=b'Data de Nascimento')),
                ('Cliente', models.ForeignKey(verbose_name=b'Cliente', to='Filme.Pessoa', null=True)),
                ('Filme_Alugar', models.ForeignKey(verbose_name=b'Filme', to='Filme.Filme', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
