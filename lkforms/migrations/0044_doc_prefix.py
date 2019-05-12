# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lkforms', '0043_doc'),
    ]

    operations = [
        migrations.AddField(
            model_name='doc',
            name='prefix',
            field=models.CharField(default='', unique=True, max_length=10, verbose_name=b'\xd0\xa3\xd0\xbd\xd0\xb8\xd0\xba\xd0\xb0\xd0\xbb\xd1\x8c\xd0\xbd\xd1\x8b\xd0\xb9 \xd0\xbf\xd1\x80\xd0\xb5\xd1\x84\xd0\xb8\xd0\xba\xd1\x81'),
            preserve_default=False,
        ),
    ]
