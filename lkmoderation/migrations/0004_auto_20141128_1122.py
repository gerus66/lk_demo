# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lkmoderation', '0003_auto_20141127_1752'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request',
            name='comms',
        ),
        migrations.AddField(
            model_name='mform',
            name='comms',
            field=models.TextField(default='', verbose_name=b'\xd0\x9a\xd0\xbe\xd0\xbc\xd0\xbc\xd0\xb5\xd0\xbd\xd1\x82\xd0\xb0\xd1\x80\xd0\xb8\xd0\xb8', blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='mfmqn',
            name='form',
            field=models.ForeignKey(related_name='mfmqn_fmlist', verbose_name=b'\xd0\xa4\xd0\xbe\xd1\x80\xd0\xbc\xd0\xb0 \xd0\xb4\xd0\xbb\xd1\x8f \xd0\xbf\xd1\x80\xd0\xb5\xd0\xb4\xd1\x81\xd1\x82\xd0\xb0\xd0\xb2\xd0\xbb\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f \xd0\xba \xd0\xbc\xd0\xbe\xd0\xb4\xd0\xb5\xd1\x80\xd0\xb0\xd1\x86\xd0\xb8\xd0\xb8', to='lkmoderation.MForm'),
            preserve_default=True,
        ),
    ]
