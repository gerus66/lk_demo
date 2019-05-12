# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('lkforum', '0009_qnans_topic'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='default_receiver',
            field=models.ForeignKey(default=3, verbose_name=b'\xd0\x90\xd0\xb4\xd1\x80\xd0\xb5\xd1\x81\xd0\xb0\xd1\x82 \xd0\xbf\xd0\xbe \xd1\x83\xd0\xbc\xd0\xbe\xd0\xbb\xd1\x87\xd0\xb0\xd0\xbd\xd0\xb8\xd1\x8e', to='lkforum.Receiver'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='receiver',
            name='user',
            field=models.ForeignKey(related_name='receiver_profile', verbose_name=b'\xd0\x9b\xd0\xbe\xd0\xb3\xd0\xb8\xd0\xbd', to=settings.AUTH_USER_MODEL, unique=True),
            preserve_default=True,
        ),
    ]
