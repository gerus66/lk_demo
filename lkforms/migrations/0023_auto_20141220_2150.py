# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import lkforms.models


class Migration(migrations.Migration):

    dependencies = [
        ('lkforms', '0022_form_not_reversed'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='external',
            options={'verbose_name': '\u0412\u043d\u0435\u0448\u043d\u0438\u0435 \u0434\u0430\u043d\u043d\u044b\u0435', 'verbose_name_plural': '\u0412\u043d\u0435\u0448\u043d\u0438\u0435 \u0434\u0430\u043d\u043d\u044b\u0435'},
        ),
        migrations.AddField(
            model_name='external',
            name='for_mail',
            field=models.BooleanField(default=False, verbose_name=b'\xd0\xa0\xd0\xb0\xd1\x81\xd1\x81\xd1\x8b\xd0\xbb\xd0\xba\xd0\xb0 \xd0\xbf\xd0\xb8\xd1\x81\xd0\xb5\xd0\xbc'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='external',
            name='letter',
            field=models.TextField(default=b'', verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xba\xd1\x81\xd1\x82 \xd0\xbf\xd0\xb8\xd1\x81\xd1\x8c\xd0\xbc\xd0\xb0', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='external',
            name='exfile',
            field=models.FileField(help_text=b'\xd0\xa4\xd0\xb0\xd0\xb9\xd0\xbb \xd1\x84\xd0\xbe\xd1\x80\xd0\xbc\xd0\xb0\xd1\x82\xd0\xb0 .csv \xd1\x81 \xd0\xba\xd0\xbe\xd0\xbb\xd0\xbe\xd0\xbd\xd0\xba\xd0\xb0\xd0\xbc\xd0\xb8: \xd0\xa4/\xd0\x98/\xd0\x9e/\xd0\x94.\xd1\x80./(id_\xd0\xb2\xd0\xbe\xd0\xbf\xd1\x80\xd0\xbe\xd1\x81\xd0\xb0.[\xd0\xbb\xd1\x8e\xd0\xb1\xd0\xbe\xd0\xb9 \xd1\x82\xd0\xb5\xd0\xba\xd1\x81\xd1\x82] - \xd0\xb4\xd0\xbb\xd1\x8f \xd0\xb7\xd0\xb0\xd0\xb3\xd1\x80\xd1\x83\xd0\xb7\xd0\xba\xd0\xb8 \xd0\xbe\xd1\x82\xd0\xb2\xd0\xb5\xd1\x82\xd0\xbe\xd0\xb2)', upload_to=lkforms.models.exfile_path, verbose_name=b'\xd0\xa4\xd0\xb0\xd0\xb9\xd0\xbb'),
            preserve_default=True,
        ),
    ]
