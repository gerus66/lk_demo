# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lkforms', '0023_auto_20141220_2150'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='external',
            name='for_mail',
        ),
    ]
