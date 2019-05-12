# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lkforms', '0025_external_letter_abs'),
    ]

    operations = [
        migrations.AddField(
            model_name='fmqn',
            name='is_priv',
            field=models.BooleanField(default=False, verbose_name=b'\xd0\xa1\xd0\xba\xd1\x80\xd1\x8b\xd1\x82\xd1\x8b\xd0\xb9'),
            preserve_default=True,
        ),
    ]
