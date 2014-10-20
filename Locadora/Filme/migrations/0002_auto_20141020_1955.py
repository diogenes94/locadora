# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Filme', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filme',
            name='Categoria',
            field=models.CharField(max_length=20, null=True, verbose_name=b'Categoria', choices=[(b'Lan\xc3\xa7amento', b'Lan\xc3\xa7amento'), (b'Promocao', b'Promo\xc3\xa7\xc3\xa3o'), (b'SD', b'Sem Descontos')]),
        ),
        migrations.AlterField(
            model_name='filme',
            name='Classificacao',
            field=models.CharField(max_length=20, null=True, verbose_name=b'Classifica\xc3\xa7\xc3\xa3o', choices=[(b'Terror', b'Terror'), (b'Acao', b'A\xc3\xa7\xc3\xa3o'), (b'Com\xc3\xa9dia', b'Com\xc3\xa9dia'), (b'Er\xc3\xb3tico', b'Er\xc3\xb3tico'), (b'Romance', b'Romance'), (b'Anima\xc3\xa7\xc3\xa3o', b'Anima\xc3\xa7\xc3\xa3o'), (b'Suspense', b'Suspense')]),
        ),
        migrations.AlterField(
            model_name='filme',
            name='Nome_Filme',
            field=models.CharField(max_length=100, null=True, verbose_name=b'Nome do Filme'),
        ),
    ]
