# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lkforms', '0045_doc_list_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='year',
            field=models.IntegerField(default=b'0', verbose_name=b'\xd0\x93\xd0\xbe\xd0\xb4 \xd0\xb2\xd1\x8b\xd0\xbf\xd1\x83\xd1\x81\xd0\xba\xd0\xb0'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='form',
            name='not_reversed',
            field=models.BooleanField(default=False, verbose_name=b'\xd0\x9d\xd0\xb5\xd0\xb2\xd0\xbe\xd0\xb7\xd0\xb2\xd1\x80\xd0\xb0\xd1\x82\xd0\xbd\xd0\xb0\xd1\x8f'),
            preserve_default=True,
        ),
    ]
