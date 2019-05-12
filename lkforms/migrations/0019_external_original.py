# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lkforms', '0018_auto_20141212_1059'),
    ]

    operations = [
        migrations.AddField(
            model_name='external',
            name='original',
            field=models.CharField(default='', max_length=50, verbose_name=b'\xd0\x9e\xd1\x80\xd0\xb8\xd0\xb3\xd0\xb8\xd0\xbd\xd0\xb0\xd0\xbb\xd1\x8c\xd0\xbd\xd0\xbe\xd0\xb5 \xd0\xbd\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5', blank=True),
            preserve_default=False,
        ),
    ]
