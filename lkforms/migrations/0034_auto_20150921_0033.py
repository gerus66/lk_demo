# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lkforms', '0033_auto_20150921_0008'),
    ]

    operations = [
        migrations.RenameField(
            model_name='form',
            old_name='test_anwers',
            new_name='test_answers',
        ),
    ]
