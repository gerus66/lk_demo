# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lkforms', '0029_auto_20150217_1136'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='theme',
            field=models.ForeignKey(related_name='form_list', default=1, to='lkforms.Theme'),
            preserve_default=False,
        ),
    ]
