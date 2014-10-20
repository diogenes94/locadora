# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Filme', '0002_auto_20141020_1955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filme',
            name='Categoria',
            field=models.CharField(max_length=20, null=True, verbose_name=b'Categoria', choices=[(b'Lancamento', b'Lan\xc3\xa7amento'), (b'Promocao', b'Promo\xc3\xa7\xc3\xa3o'), (b'SD', b'Sem Descontos')]),
        ),
        migrations.AlterField(
            model_name='filme',
            name='Classificacao',
            field=models.CharField(max_length=20, null=True, verbose_name=b'Classifica\xc3\xa7\xc3\xa3o', choices=[(b'Terror', b'Terror'), (b'Acao', b'A\xc3\xa7\xc3\xa3o'), (b'Comedia', b'Com\xc3\xa9dia'), (b'Erotico', b'Er\xc3\xb3tico'), (b'Romance', b'Romance'), (b'Animacao', b'Anima\xc3\xa7\xc3\xa3o'), (b'Suspense', b'Suspense')]),
        ),
    ]
