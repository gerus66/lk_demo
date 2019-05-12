# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lkforms', '0024_remove_external_for_mail'),
    ]

    operations = [
        migrations.AddField(
            model_name='external',
            name='letter_abs',
            field=models.CharField(default=b'', max_length=50, verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xbc\xd0\xb0 \xd0\xbf\xd0\xb8\xd1\x81\xd1\x8c\xd0\xbc\xd0\xb0', blank=True),
            preserve_default=True,
        ),
    ]
