# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import lkforms.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lkforms', '0011_auto_20141124_1631'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='owner',
            field=models.ForeignKey(verbose_name=b'\xd0\x92\xd0\xbb\xd0\xb0\xd0\xb4\xd0\xb5\xd0\xbb\xd0\xb5\xd1\x86', blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='external',
            name='exfile',
            field=models.FileField(help_text=b'\xd0\xa4\xd0\xb0\xd0\xb9\xd0\xbb \xd1\x84\xd0\xbe\xd1\x80\xd0\xbc\xd0\xb0\xd1\x82\xd0\xb0 .csv \xd1\x81 \xd0\xba\xd0\xbe\xd0\xbb\xd0\xbe\xd0\xbd\xd0\xba\xd0\xb0\xd0\xbc\xd0\xb8: \xd0\xa4/\xd0\x98/\xd0\x9e/\xd0\x94.\xd1\x80./id_\xd0\xb2\xd0\xbe\xd0\xbf\xd1\x80\xd0\xbe\xd1\x81\xd0\xb0.[\xd0\xbb\xd1\x8e\xd0\xb1\xd0\xbe\xd0\xb9 \xd1\x82\xd0\xb5\xd0\xba\xd1\x81\xd1\x82]', upload_to=lkforms.models.exfile_path, verbose_name=b'\xd0\xa4\xd0\xb0\xd0\xb9\xd0\xbb'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='form',
            name='result',
            field=models.FileField(help_text=b'\xd0\xa4\xd0\xb0\xd0\xb9\xd0\xbb \xd1\x84\xd0\xbe\xd1\x80\xd0\xbc\xd0\xb0\xd1\x82\xd0\xb0 .csv \xd1\x81 \xd0\xba\xd0\xbe\xd0\xbb\xd0\xbe\xd0\xbd\xd0\xba\xd0\xb0\xd0\xbc\xd0\xb8: \xd0\xa4/\xd0\x98/\xd0\x9e/\xd0\x94.\xd1\x80./\xd0\x97\xd0\xb0\xd1\x87\xd0\xb5\xd1\x82/\xd0\xa0\xd0\xb5\xd0\xb7\xd0\xb5\xd1\x80\xd0\xb2/\xd0\x9d\xd0\xb5\xd0\xb7\xd0\xb0\xd1\x87\xd0\xb5\xd1\x82/[[Priv ]\xd0\xbb\xd1\x8e\xd0\xb1\xd0\xbe\xd0\xb9 \xd1\x82\xd0\xb5\xd0\xba\xd1\x81\xd1\x82]', upload_to=lkforms.models.result_path, verbose_name=b'\xd0\xa0\xd0\xb5\xd0\xb7\xd1\x83\xd0\xbb\xd1\x8c\xd1\x82\xd0\xb0\xd1\x82\xd1\x8b', blank=True),
            preserve_default=True,
        ),
    ]