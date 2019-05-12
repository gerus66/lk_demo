# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lkforms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='sex',
            field=models.PositiveSmallIntegerField(default=b'0', verbose_name=b'\xd0\x9f\xd0\xbe\xd0\xbb', choices=[(0, b'\xd0\xb2\xd1\x8b\xd0\xb1\xd1\x80\xd0\xb0\xd1\x82\xd1\x8c'), (b'f', b'\xd0\xb6\xd0\xb5\xd0\xbd'), (b'm', b'\xd0\xbc\xd1\x83\xd0\xb6')]),
            preserve_default=True,
        ),
    ]
