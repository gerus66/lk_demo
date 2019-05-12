# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lkforms', '0032_auto_20150315_1248'),
        ('lkmoderation', '0016_auto_20141212_1745'),
    ]

    operations = [
        migrations.AddField(
            model_name='mform',
            name='theme',
            field=models.ForeignKey(default=1, verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xbc\xd0\xb0', to='lkforms.Theme'),
            preserve_default=False,
        ),
    ]
