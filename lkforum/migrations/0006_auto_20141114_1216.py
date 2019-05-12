# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lkforum', '0005_qnans_receiver'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receiver',
            name='position',
        ),
        migrations.AddField(
            model_name='receiver',
            name='post',
            field=models.CharField(default=2, unique=True, max_length=250, verbose_name=b'\xd0\x94\xd0\xbe\xd0\xbb\xd0\xb6\xd0\xbd\xd0\xbe\xd1\x81\xd1\x82\xd1\x8c'),
            preserve_default=False,
        ),
    ]
