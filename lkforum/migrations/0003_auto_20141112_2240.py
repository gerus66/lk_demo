# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('lkforum', '0002_auto_20141112_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qnans',
            name='user',
            field=models.ForeignKey(verbose_name=b'\xd0\x90\xd0\xb2\xd1\x82\xd0\xbe\xd1\x80 \xd0\xb2\xd0\xbe\xd0\xbf\xd1\x80\xd0\xbe\xd1\x81\xd0\xb0', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
