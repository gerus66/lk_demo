# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lkforms', '0035_auto_20160519_2250'),
    ]

    operations = [
        migrations.AddField(
            model_name='external',
            name='is_utf',
            field=models.BooleanField(default=False, verbose_name=b'UTF-8'),
            preserve_default=True,
        ),
    ]
