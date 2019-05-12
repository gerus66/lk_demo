# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import lkforms.models


class Migration(migrations.Migration):

    dependencies = [
        ('lkforms', '0017_form_reader'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='clarification',
            field=models.TextField(default='', verbose_name=b'\xd0\x9f\xd0\xbe\xd1\x8f\xd1\x81\xd0\xbd\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f', blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='form',
            name='default_list',
            field=models.FileField(help_text=b'\xd0\xa4\xd0\xb0\xd0\xb9\xd0\xbb \xd1\x84\xd0\xbe\xd1\x80\xd0\xbc\xd0\xb0\xd1\x82\xd0\xb0 .csv \xd1\x81 \xd0\xba\xd0\xbe\xd0\xbb\xd0\xbe\xd0\xbd\xd0\xba\xd0\xb0\xd0\xbc\xd0\xb8: \xd0\xa4/\xd0\x98/\xd0\x9e/\xd0\x94.\xd1\x80.', upload_to=lkforms.models.default_list_path, verbose_name=b'\xd0\xad\xd1\x82\xd0\xb0\xd0\xbb\xd0\xbe\xd0\xbd\xd0\xbd\xd1\x8b\xd0\xb9 \xd1\x81\xd0\xbf\xd0\xb8\xd1\x81\xd0\xbe\xd0\xba', blank=True),
            preserve_default=True,
        ),
    ]
