# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Filme', '0007_auto_20141020_2023'),
    ]

    operations = [
        migrations.AddField(
            model_name='filme',
            name='Preco',
            field=models.DecimalField(null=True, verbose_name=b'Pre\xc3\xa7o', max_digits=10, decimal_places=2),
            preserve_default=True,
        ),
    ]
