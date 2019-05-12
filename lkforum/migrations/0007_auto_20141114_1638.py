# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lkforum', '0006_auto_20141114_1216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receiver',
            name='extra_email',
            field=models.CharField(default=b'', max_length=250, verbose_name=b'\xd0\x94\xd0\xbe\xd0\xbf\xd0\xbe\xd0\xbb\xd0\xbd\xd0\xb8\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8c\xd0\xbd\xd1\x8b\xd0\xb9 e-mail', blank=True),
            preserve_default=True,
        ),
    ]
