# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lkforms', '0008_auto_20141116_2135'),
    ]

    operations = [
        migrations.AddField(
            model_name='fmqn',
            name='number',
            field=models.CharField(default=b'', max_length=3, verbose_name=b'\xd0\x9d\xd0\xbe\xd0\xbc\xd0\xb5\xd1\x80 \xd0\xb2\xd0\xbe\xd0\xbf\xd1\x80\xd0\xbe\xd1\x81\xd0\xb0', blank=True),
            preserve_default=True,
        ),
    ]
