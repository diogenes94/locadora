# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Filme', '0009_auto_20141020_2035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='NomeCategoria',
            field=models.CharField(max_length=20, null=True, verbose_name=b'Categoria'),
        ),
    ]
