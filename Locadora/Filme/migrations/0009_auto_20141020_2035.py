# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Filme', '0008_filme_preco'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('NomeCategoria', models.CharField(max_length=20, null=True, verbose_name=b'Categoria', choices=[(b'Lancamento', b'Lan\xc3\xa7amento'), (b'Promocao', b'Promo\xc3\xa7\xc3\xa3o'), (b'SD', b'Sem Descontos')])),
                ('Preco', models.DecimalField(null=True, verbose_name=b'Pre\xc3\xa7o', max_digits=10, decimal_places=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='filme',
            name='Preco',
        ),
        migrations.AlterField(
            model_name='filme',
            name='Categoria',
            field=models.ForeignKey(verbose_name=b'Categoria', to='Filme.Categoria', null=True),
        ),
    ]
