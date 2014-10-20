# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Filme',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Nome_Filme', models.CharField(max_length=100, null=True, verbose_name=b'Nome')),
                ('Classificacao', models.CharField(max_length=20, null=True, verbose_name=b'Classifica\xc3\xa7\xc3\xa3o', choices=[(b'Terror', b'Terror'), (b'A\xc3\xa7\xc3\xa3o', b'A\xc3\xa7\xc3\xa3o'), (b'Com\xc3\xa9dia', b'Com\xc3\xa9dia'), (b'Er\xc3\xb3tico', b'Er\xc3\xb3tico'), (b'Romance', b'Romance'), (b'Anima\xc3\xa7\xc3\xa3o', b'Anima\xc3\xa7\xc3\xa3o'), (b'Suspense', b'Suspense')])),
                ('Categoria', models.CharField(max_length=20, null=True, verbose_name=b'Categoria', choices=[(b'Lan\xc3\xa7amento', b'Lan\xc3\xa7amento'), (b'Promo\xc3\xa7\xc3\xa3o', b'Promo\xc3\xa7\xc3\xa3o'), (b'Sem Descontos', b'Sem Descontos')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
