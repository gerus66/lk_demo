# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lkforms', '0006_auto_20141106_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='file',
            field=models.FileField(upload_to=b'for_users', verbose_name=b'\xd0\xa4\xd0\xb0\xd0\xb9\xd0\xbb', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='regres',
            name='short_result',
            field=models.PositiveSmallIntegerField(default=0, verbose_name=b'\xd0\xa0\xd0\xb5\xd0\xb7\xd1\x83\xd0\xbb\xd1\x8c\xd1\x82\xd0\xb0\xd1\x82', choices=[(0, b'\xd0\xbd\xd0\xb5\xd0\xbe\xd0\xbf\xd1\x80\xd0\xb5\xd0\xb4\xd0\xb5\xd0\xbb\xd0\xb5\xd0\xbd'), (1, b'\xd0\xb7\xd0\xb0\xd1\x87\xd0\xb5\xd1\x82'), (2, b'\xd0\xbd\xd0\xb5\xd0\xb7\xd0\xb0\xd1\x87\xd0\xb5\xd1\x82'), (3, b'\xd0\xb2 \xd1\x80\xd0\xb5\xd0\xb7\xd0\xb5\xd1\x80\xd0\xb2\xd0\xb5')]),
            preserve_default=True,
        ),
    ]
