# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lkforms', '0009_fmqn_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='External',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'\xd1\x81\xd0\xbe\xd0\xb7\xd0\xb4\xd0\xb0\xd0\xbd')),
                ('changed', models.DateTimeField(auto_now=True, verbose_name=b'\xd0\xb8\xd0\xb7\xd0\xbc\xd0\xb5\xd0\xbd\xd0\xb5\xd0\xbd')),
                ('exfile', models.FileField(help_text=b'\xd0\xa4\xd0\xb0\xd0\xb9\xd0\xbb \xd1\x81 \xd0\xbd\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5\xd0\xbc \xd0\xb2\xd0\xb8\xd0\xb4\xd0\xb0 ext_[id \xd1\x84\xd0\xbe\xd1\x80\xd0\xbc\xd1\x8b]_[\xd0\xbb\xd1\x8e\xd0\xb1\xd0\xbe\xd0\xb9 \xd1\x82\xd0\xb5\xd0\xba\xd1\x81\xd1\x82].csv \xd0\xb8 \xd0\xba\xd0\xbe\xd0\xbb\xd0\xbe\xd0\xbd\xd0\xba\xd0\xb0\xd0\xbc\xd0\xb8: \xd0\xa4/\xd0\x98/\xd0\x9e/\xd0\x94.\xd1\x80./[id_\xd0\xb2\xd0\xbe\xd0\xbf\xd1\x80\xd0\xbe\xd1\x81\xd0\xb0].[\xd0\xbb\xd1\x8e\xd0\xb1\xd0\xbe\xd0\xb9 \xd1\x82\xd0\xb5\xd0\xba\xd1\x81\xd1\x82]', upload_to=b'external', verbose_name=b'\xd0\x94\xd0\xb0\xd0\xbd\xd0\xbd\xd1\x8b\xd0\xb5 \xd0\xb8\xd0\xb7\xd0\xb2\xd0\xbd\xd0\xb5')),
            ],
            options={
                'verbose_name': '\u0424\u0430\u0439\u043b \u0434\u0430\u043d\u043d\u044b\u0445 \u0438\u0437\u0432\u043d\u0435',
                'verbose_name_plural': '\u0424\u0430\u0439\u043b\u044b \u0434\u0430\u043d\u043d\u044b\u0445 \u0438\u0437\u0432\u043d\u0435',
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='form',
            name='external',
        ),
    ]
