# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Filme', '0010_auto_20141020_2037'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pessoa',
            name='Email',
        ),
    ]
