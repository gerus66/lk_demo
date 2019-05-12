# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lkmoderation', '0008_mquestion_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mfmmqn',
            name='form',
        ),
        migrations.RemoveField(
            model_name='mfmmqn',
            name='question',
        ),
        migrations.DeleteModel(
            name='MFmMQn',
        ),
        migrations.RemoveField(
            model_name='mvariant',
            name='question',
        ),
        migrations.DeleteModel(
            name='MVariant',
        ),
        migrations.RemoveField(
            model_name='mquestion',
            name='comms',
        ),
        migrations.RemoveField(
            model_name='mquestion',
            name='multi_vars',
        ),
        migrations.RemoveField(
            model_name='mquestion',
            name='not_blank',
        ),
        migrations.RemoveField(
            model_name='mquestion',
            name='owner',
        ),
        migrations.AddField(
            model_name='mquestion',
            name='form',
            field=models.ForeignKey(related_name='qns_list', default=11, verbose_name=b'\xd0\xa4\xd0\xbe\xd1\x80\xd0\xbc\xd0\xb0 \xd0\xb4\xd0\xbb\xd1\x8f \xd0\xbf\xd1\x80\xd0\xb5\xd0\xb4\xd1\x81\xd1\x82\xd0\xb0\xd0\xb2\xd0\xbb\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f \xd0\xba \xd0\xbc\xd0\xbe\xd0\xb4\xd0\xb5\xd1\x80\xd0\xb0\xd1\x86\xd0\xb8\xd0\xb8', to='lkmoderation.MForm'),
            preserve_default=False,
        ),
    ]
