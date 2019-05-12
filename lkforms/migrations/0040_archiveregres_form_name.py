# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lkforms', '0039_remove_archiveanswer_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='archiveregres',
            name='form_name',
            field=models.CharField(default=b'', max_length=250, verbose_name=b'\xd0\xa4\xd0\xbe\xd1\x80\xd0\xbc\xd0\xb0', blank=True),
            preserve_default=True,
        ),
    ]
