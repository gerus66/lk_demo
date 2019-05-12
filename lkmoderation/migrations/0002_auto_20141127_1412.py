# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lkmoderation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mform',
            name='syn_form',
            field=models.ForeignKey(null=True, blank=True, to='lkforms.Form', unique=True, verbose_name=b'\xd0\xa4\xd0\xbe\xd1\x80\xd0\xbc\xd0\xb0 \xd1\x81\xd0\xb8\xd0\xbd\xd1\x85\xd1\x80\xd0\xbe\xd0\xbd\xd0\xb8\xd0\xb7\xd0\xb0\xd1\x86\xd0\xb8\xd0\xb8'),
            preserve_default=True,
        ),
    ]
