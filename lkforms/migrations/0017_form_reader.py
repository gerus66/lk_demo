# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lkforms', '0016_auto_20141204_1603'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='reader',
            field=models.ManyToManyField(related_name='read_forms', null=True, verbose_name=b'Readers', to=settings.AUTH_USER_MODEL, blank=True),
            preserve_default=True,
        ),
    ]
