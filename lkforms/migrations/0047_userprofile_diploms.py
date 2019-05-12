# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lkforms', '0046_auto_20180808_1605'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='diploms',
            field=models.TextField(default=b'', verbose_name=b'\xd0\x94\xd0\xb8\xd0\xbf\xd0\xbb\xd0\xbe\xd0\xbc\xd1\x8b'),
            preserve_default=True,
        ),
    ]
