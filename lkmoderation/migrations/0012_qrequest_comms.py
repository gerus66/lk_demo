# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lkmoderation', '0011_auto_20141204_1603'),
    ]

    operations = [
        migrations.AddField(
            model_name='qrequest',
            name='comms',
            field=models.TextField(default='', verbose_name=b'\xd0\x9a\xd0\xbe\xd0\xbc\xd0\xbc\xd0\xb5\xd0\xbd\xd1\x82\xd0\xb0\xd1\x80\xd0\xb8\xd0\xb8', blank=True),
            preserve_default=False,
        ),
    ]
