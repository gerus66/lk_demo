# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lkforms', '0019_external_original'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='external',
            name='original',
        ),
    ]
