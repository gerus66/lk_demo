# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lkforum', '0003_auto_20141112_2240'),
    ]

    operations = [
        migrations.CreateModel(
            name='Receiver',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'\xd1\x81\xd0\xbe\xd0\xb7\xd0\xb4\xd0\xb0\xd0\xbd')),
                ('changed', models.DateTimeField(auto_now=True, verbose_name=b'\xd0\xb8\xd0\xb7\xd0\xbc\xd0\xb5\xd0\xbd\xd0\xb5\xd0\xbd')),
                ('position', models.TextField(verbose_name=b'\xd0\x94\xd0\xbe\xd0\xbb\xd0\xb6\xd0\xbd\xd0\xbe\xd1\x81\xd1\x82\xd1\x8c')),
                ('extra_email', models.TextField(default=b'', verbose_name=b'\xd0\x94\xd0\xbe\xd0\xbf\xd0\xbe\xd0\xbb\xd0\xbd\xd0\xb8\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8c\xd0\xbd\xd1\x8b\xd0\xb9 e-mail', blank=True)),
                ('user', models.ForeignKey(verbose_name=b'\xd0\x9b\xd0\xbe\xd0\xb3\xd0\xb8\xd0\xbd', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u0410\u0434\u0440\u0435\u0441\u0430\u0442 \u0432\u043e\u043f\u0440\u043e\u0441\u043e\u0432',
                'verbose_name_plural': '\u0410\u0434\u0440\u0435\u0441\u0430\u0442\u044b \u0432\u043e\u043f\u0440\u043e\u0441\u043e\u0432',
            },
            bases=(models.Model,),
        ),
        migrations.RenameField(
            model_name='qnans',
            old_name='user',
            new_name='author',
        ),
    ]
