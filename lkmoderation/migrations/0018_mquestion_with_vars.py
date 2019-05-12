# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lkmoderation', '0017_mform_theme'),
    ]

    operations = [
        migrations.AddField(
            model_name='mquestion',
            name='with_vars',
            field=models.BooleanField(default=False, verbose_name=b'\xd0\xa1 \xd0\xb2\xd0\xb0\xd1\x80\xd0\xb8\xd0\xb0\xd0\xbd\xd1\x82\xd0\xb0\xd0\xbc\xd0\xb8 \xd0\xbe\xd1\x82\xd0\xb2\xd0\xb5\xd1\x82\xd0\xb0'),
            preserve_default=True,
        ),
    ]
