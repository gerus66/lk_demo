# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lkforms', '0021_auto_20141214_1651'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='not_reversed',
            field=models.BooleanField(default=False, verbose_name=b'\xd0\xa3\xd0\xbf\xd1\x80\xd0\xb0\xd0\xb2\xd0\xbb\xd1\x8f\xd1\x8e\xd1\x89\xd0\xb0\xd1\x8f'),
            preserve_default=True,
        ),
    ]
