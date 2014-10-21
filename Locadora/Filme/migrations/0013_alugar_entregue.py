# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Filme', '0012_auto_20141020_2140'),
    ]

    operations = [
        migrations.AddField(
            model_name='alugar',
            name='Entregue',
            field=models.CharField(default=False, max_length=3, verbose_name=b'Status de Entrega', choices=[(b'False', b'N\xc3\xa3o'), (b'True', b'Sim')]),
            preserve_default=True,
        ),
    ]
