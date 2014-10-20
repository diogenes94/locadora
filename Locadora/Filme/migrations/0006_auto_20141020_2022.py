# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Filme', '0005_aluga'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alugar',
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
        migrations.RemoveField(
            model_name='aluga',
            name='Cliente',
        ),
        migrations.RemoveField(
            model_name='aluga',
            name='Filme_Alugar',
        ),
        migrations.DeleteModel(
            name='Aluga',
        ),
    ]
