# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lkmoderation', '0013_auto_20141204_1705'),
    ]

    operations = [
        migrations.AddField(
            model_name='mform',
            name='reader',
            field=models.ManyToManyField(related_name='read_mforms', null=True, verbose_name=b'Readers', to=settings.AUTH_USER_MODEL, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='request',
            name='type',
            field=models.PositiveSmallIntegerField(default=b'0', verbose_name=b'\xd0\xa2\xd0\xb8\xd0\xbf \xd0\xb7\xd0\xb0\xd0\xbf\xd1\x80\xd0\xbe\xd1\x81\xd0\xb0', choices=[(0, b'\xd1\x83\xd0\xb4\xd0\xb0\xd0\xbb\xd0\xb8\xd1\x82\xd1\x8c'), (1, b'\xd1\x81\xd0\xbe\xd0\xb7\xd0\xb4\xd0\xb0\xd1\x82\xd1\x8c'), (2, b'\xd1\x81\xd0\xb8\xd0\xbd\xd1\x85\xd1\x80\xd0\xbe\xd0\xbd\xd0\xb8\xd0\xb7\xd0\xb8\xd1\x80\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x82\xd1\x8c'), (3, b'\xd1\x80\xd0\xb5\xd0\xb3\xd0\xb8\xd1\x81\xd1\x82\xd1\x80\xd0\xb0\xd1\x86\xd0\xb8\xd0\xb8 \xd0\xb2 \xd0\xb0\xd1\x80\xd1\x85\xd0\xb8\xd0\xb2'), (4, b'\xd1\x80\xd0\xb5\xd0\xb7\xd1\x83\xd0\xbb\xd1\x8c\xd1\x82\xd0\xb0\xd1\x82\xd1\x8b \xd0\xb2 \xd0\xb0\xd1\x80\xd1\x85\xd0\xb8\xd0\xb2')]),
            preserve_default=True,
        ),
    ]
