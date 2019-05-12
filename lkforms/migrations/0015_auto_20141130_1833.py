# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lkforms', '0014_auto_20141128_1530'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='just_user',
            field=models.ManyToManyField(related_name='use_forms', null=True, verbose_name=b'Editors', to=settings.AUTH_USER_MODEL, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='form',
            name='editor',
            field=models.ManyToManyField(related_name='edit_forms', null=True, verbose_name=b'Editors', to=settings.AUTH_USER_MODEL, blank=True),
            preserve_default=True,
        ),
    ]
