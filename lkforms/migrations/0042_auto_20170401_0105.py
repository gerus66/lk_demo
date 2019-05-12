# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('lkforms', '0041_auto_20161121_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='external',
            name='owner',
            field=models.ForeignKey(related_name='own_external', verbose_name=b'\xd0\x92\xd0\xbb\xd0\xb0\xd0\xb4\xd0\xb5\xd0\xbb\xd0\xb5\xd1\x86', to=settings.AUTH_USER_MODEL, help_text=b'\xd0\x92 \xd1\x81\xd0\xbf\xd0\xb8\xd1\x81\xd0\xba\xd0\xb5 \xd0\xb2\xd1\x8b\xd0\xb1\xd0\xbe\xd1\x80\xd0\xb0 \xd1\x82\xd0\xbe\xd0\xbb\xd1\x8c\xd0\xba\xd0\xbe \xd0\xbf\xd0\xbe\xd0\xbb\xd1\x8c\xd0\xb7\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x82\xd0\xb5\xd0\xbb\xd0\xb8, \xd0\xbe\xd0\xb1\xd0\xbb\xd0\xb0\xd0\xb4\xd0\xb0\xd1\x8e\xd1\x89\xd0\xb8\xd0\xb5 \xd1\x81\xd1\x82\xd0\xb0\xd1\x82\xd1\x83\xd1\x81\xd0\xbe\xd0\xbc \xd0\xbf\xd0\xb5\xd1\x80\xd1\x81\xd0\xbe\xd0\xbd\xd0\xb0\xd0\xbb\xd0\xb0 \xd0\xb8 \xd1\x81\xd0\xbe\xd1\x81\xd1\x82\xd0\xbe\xd1\x8f\xd1\x89\xd0\xb8\xd0\xb5 \xd0\xb2 \xd0\xb3\xd1\x80\xd1\x83\xd0\xbf\xd0\xbf\xd0\xb5 \xd0\x90\xd0\xb4\xd0\xbc\xd0\xb8\xd0\xbd\xd0\xb8\xd1\x81\xd1\x82\xd1\x80\xd0\xb0\xd1\x82\xd0\xbe\xd1\x80\xd1\x8b'),
            preserve_default=True,
        ),
    ]
