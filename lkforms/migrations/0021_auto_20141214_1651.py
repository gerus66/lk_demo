# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lkforms', '0020_remove_external_original'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='external',
            options={'verbose_name': '\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0432\u043d\u0435\u0448\u043d\u0438\u0435 \u0434\u0430\u043d\u043d\u044b\u0435', 'verbose_name_plural': '\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0432\u043d\u0435\u0448\u043d\u0438\u0435 \u0434\u0430\u043d\u043d\u044b\u0435'},
        ),
        migrations.AddField(
            model_name='external',
            name='original',
            field=models.CharField(default='', max_length=250, verbose_name=b'\xd0\x9f\xd0\xbe\xd1\x8f\xd1\x81\xd0\xbd\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f'),
            preserve_default=False,
        ),
    ]
