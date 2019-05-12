# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lkforms', '0047_userprofile_diploms'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='clarification_eng',
            field=models.CharField(default=b'', max_length=250, verbose_name=b'English version of clarification', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='form',
            name='full_name_eng',
            field=models.CharField(default=b'', max_length=250, verbose_name=b'English version of full_name', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='form',
            name='name_eng',
            field=models.CharField(default=b'', max_length=250, verbose_name=b'English version of name', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='question',
            name='eng',
            field=models.TextField(default=b'', verbose_name=b'English version', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='variant',
            name='eng',
            field=models.CharField(default=b'', max_length=250, verbose_name=b'English version', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='year',
            field=models.IntegerField(default=b'0', help_text=b'1900 - \xd0\xb4\xd0\xbb\xd1\x8f \xd0\xb2\xd0\xb7\xd1\x80\xd0\xbe\xd1\x81\xd0\xbb\xd1\x8b\xd1\x85, 2100 - \xd0\xb4\xd0\xbb\xd1\x8f \xd0\xbc\xd0\xb0\xd0\xbb\xd0\xb5\xd0\xbd\xd1\x8c\xd0\xba\xd0\xb8\xd1\x85', verbose_name=b'\xd0\x93\xd0\xbe\xd0\xb4 \xd0\xb2\xd1\x8b\xd0\xbf\xd1\x83\xd1\x81\xd0\xba\xd0\xb0'),
            preserve_default=True,
        ),
    ]
