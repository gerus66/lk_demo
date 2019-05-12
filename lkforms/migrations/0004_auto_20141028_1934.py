# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lkforms', '0003_auto_20141027_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fmqn',
            name='question',
            field=models.ForeignKey(related_name='fmqn_qnlist', verbose_name=b'\xd0\x92\xd0\xbe\xd0\xbf\xd1\x80\xd0\xbe\xd1\x81', to='lkforms.Question'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='question',
            name='comms',
            field=models.TextField(default=b'', verbose_name=b'\xd0\x9f\xd0\xbe\xd1\x8f\xd1\x81\xd0\xbd\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='variant',
            name='question',
            field=models.ForeignKey(related_name='variant_list', to='lkforms.Question'),
            preserve_default=True,
        ),
    ]
