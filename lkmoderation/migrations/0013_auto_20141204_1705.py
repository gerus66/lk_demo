# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lkmoderation', '0012_qrequest_comms'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mfmqn',
            name='question',
            field=models.ForeignKey(related_name='mfmqn_qnlist', verbose_name=b'\xd0\x92\xd0\xbe\xd0\xbf\xd1\x80\xd0\xbe\xd1\x81', to='lkforms.Question'),
            preserve_default=True,
        ),
    ]
