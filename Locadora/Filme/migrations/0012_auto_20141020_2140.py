# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Filme', '0011_remove_pessoa_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='subAluguel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Aluguel', models.ForeignKey(to='Filme.Alugar', null=True)),
                ('Filme_Alugar', models.ForeignKey(verbose_name=b'Filme', to='Filme.Filme', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='alugar',
            name='Filme_Alugar',
        ),
    ]
