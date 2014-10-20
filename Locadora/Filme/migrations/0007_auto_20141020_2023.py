# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Filme', '0006_auto_20141020_2022'),
    ]

    operations = [
        migrations.AddField(
            model_name='alugar',
            name='DataAluguel',
            field=models.DateField(null=True, verbose_name=b'Data de Loca\xc3\xa7\xc3\xa3o'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='alugar',
            name='DataEntrega',
            field=models.DateField(null=True, verbose_name=b'Data de Entrega'),
        ),
    ]
