# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lkmoderation', '0015_auto_20141211_2112'),
    ]

    operations = [
        migrations.AddField(
            model_name='mform',
            name='clarification',
            field=models.TextField(default='', verbose_name=b'\xd0\x9f\xd0\xbe\xd1\x8f\xd1\x81\xd0\xbd\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f', blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='qrequest',
            name='question',
            field=models.ForeignKey(related_name='qreq', verbose_name=b'\xd0\x92\xd0\xbe\xd0\xbf\xd1\x80\xd0\xbe\xd1\x81 \xd0\xb4\xd0\xbb\xd1\x8f \xd0\xbf\xd1\x80\xd0\xb5\xd0\xb4\xd1\x81\xd1\x82\xd0\xb0\xd0\xb2\xd0\xbb\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f \xd0\xba \xd0\xbc\xd0\xbe\xd0\xb4\xd0\xb5\xd1\x80\xd0\xb0\xd1\x86\xd0\xb8\xd0\xb8', to='lkforms.Question', unique=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='qrequest',
            name='type',
            field=models.PositiveSmallIntegerField(default=b'0', verbose_name=b'\xd0\xa2\xd0\xb8\xd0\xbf \xd0\xb7\xd0\xb0\xd0\xbf\xd1\x80\xd0\xbe\xd1\x81\xd0\xb0', choices=[(0, b'\xd1\x83\xd0\xb4\xd0\xb0\xd0\xbb\xd0\xb8\xd1\x82\xd1\x8c'), (1, b'\xd0\xb0\xd1\x80\xd1\x85\xd0\xb8\xd0\xb2\xd0\xb8\xd1\x80\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x82\xd1\x8c')]),
            preserve_default=True,
        ),
    ]
