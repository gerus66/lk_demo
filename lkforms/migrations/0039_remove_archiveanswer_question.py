# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lkforms', '0038_auto_20161002_1915'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='archiveanswer',
            name='question',
        ),
    ]
