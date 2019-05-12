# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lkforms', '0048_auto_20180923_1228'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='info_eng',
            field=models.TextField(default=b'', verbose_name=b'English version of info', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='form',
            name='clarification_eng',
            field=models.TextField(default=b'', verbose_name=b'English version of clarification', blank=True),
            preserve_default=True,
        ),
    ]
