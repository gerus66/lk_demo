# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lkforum', '0011_topic_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='number',
            field=models.CharField(default='gnrl', help_text=b'\xd0\xa2\xd0\xb5\xd0\xbc\xd1\x8b \xd1\x81 \xd0\xbe\xd0\xb4\xd0\xb8\xd0\xbd\xd0\xb0\xd0\xba\xd0\xbe\xd0\xb2\xd1\x8b\xd0\xbc \xd0\xb8\xd0\xbd\xd0\xb4\xd0\xb5\xd0\xbd\xd1\x82\xd0\xb8\xd1\x84\xd0\xb8\xd0\xba\xd0\xb0\xd1\x82\xd0\xbe\xd1\x80\xd0\xbe\xd0\xbc \xd0\xbe\xd1\x82\xd0\xbe\xd0\xb1\xd1\x80\xd0\xb0\xd0\xb6\xd0\xb0\xd1\x8e\xd1\x82\xd1\x81\xd1\x8f \xd1\x83 \xd0\xbf\xd0\xbe\xd0\xbb\xd1\x8c\xd0\xb7\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x82\xd0\xb5\xd0\xbb\xd0\xb5\xd0\xb9 \xd1\x81\xd0\xb3\xd1\x80\xd1\x83\xd0\xbf\xd0\xbf\xd0\xb8\xd1\x80\xd0\xbe\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xbd\xd1\x8b\xd0\xbc\xd0\xb8.', max_length=5, verbose_name=b'\xd0\x98\xd0\xb4\xd0\xb5\xd0\xbd\xd1\x82\xd0\xb8\xd1\x84\xd0\xb8\xd0\xba\xd0\xb0\xd1\x82\xd0\xbe\xd1\x80 \xd1\x82\xd0\xb5\xd0\xbc\xd1\x8b'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='topic',
            name='info',
            field=models.TextField(verbose_name=b'\xd0\x9e\xd0\xbf\xd0\xb8\xd1\x81\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5 \xd1\x82\xd0\xb5\xd0\xbc\xd1\x8b'),
            preserve_default=True,
        ),
    ]