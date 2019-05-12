# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lkforum', '0004_auto_20141113_1550'),
    ]

    operations = [
        migrations.AddField(
            model_name='qnans',
            name='receiver',
            field=models.ForeignKey(default=1, verbose_name=b'\xd0\x90\xd0\xb2\xd1\x82\xd0\xbe\xd1\x80 \xd0\xbe\xd1\x82\xd0\xb2\xd0\xb5\xd1\x82\xd0\xb0', to='lkforum.Receiver'),
            preserve_default=False,
        ),
    ]
