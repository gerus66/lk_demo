# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lkforum', '0008_topic'),
    ]

    operations = [
        migrations.AddField(
            model_name='qnans',
            name='topic',
            field=models.ForeignKey(default=1, verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xbc\xd0\xb0 \xd0\xb2\xd0\xbe\xd0\xbf\xd1\x80\xd0\xbe\xd1\x81\xd0\xb0', to='lkforum.Topic'),
            preserve_default=False,
        ),
    ]
