# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('lkforms', '0016_auto_20141204_1603'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lkmoderation', '0010_auto_20141203_2254'),
    ]

    operations = [
        migrations.CreateModel(
            name='QRequest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'\xd1\x81\xd0\xbe\xd0\xb7\xd0\xb4\xd0\xb0\xd0\xbd')),
                ('changed', models.DateTimeField(auto_now=True, verbose_name=b'\xd0\xb8\xd0\xb7\xd0\xbc\xd0\xb5\xd0\xbd\xd0\xb5\xd0\xbd')),
                ('type', models.PositiveSmallIntegerField(default=b'0', verbose_name=b'\xd0\xa2\xd0\xb8\xd0\xbf \xd0\xb7\xd0\xb0\xd0\xbf\xd1\x80\xd0\xbe\xd1\x81\xd0\xb0', choices=[(0, b'\xd1\x83\xd0\xb4\xd0\xb0\xd0\xbb\xd0\xb8\xd1\x82\xd1\x8c')])),
                ('passed', models.PositiveSmallIntegerField(default=b'0', verbose_name=b'\xd0\x9c\xd0\xbe\xd0\xb4\xd0\xb5\xd1\x80\xd0\xb0\xd1\x86\xd0\xb8\xd1\x8f', choices=[(0, b''), (1, b'\xd0\xbe\xd0\xb4\xd0\xbe\xd0\xb1\xd1\x80\xd0\xb5\xd0\xbd\xd0\xbe'), (2, b'\xd0\xbe\xd1\x82\xd0\xba\xd0\xbb\xd0\xbe\xd0\xbd\xd0\xb5\xd0\xbd\xd0\xbe')])),
                ('author', models.ForeignKey(related_name='qreq_list', verbose_name=b'\xd0\x90\xd0\xb2\xd1\x82\xd0\xbe\xd1\x80 \xd0\xb7\xd0\xb0\xd0\xbf\xd1\x80\xd0\xbe\xd1\x81\xd0\xb0', to=settings.AUTH_USER_MODEL)),
                ('moderator', models.ForeignKey(related_name='qmod_list', verbose_name=b'\xd0\x9c\xd0\xbe\xd0\xb4\xd0\xb5\xd1\x80\xd0\xb0\xd1\x82\xd0\xbe\xd1\x80', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('question', models.ForeignKey(related_name='qreq', verbose_name=b'\xd0\x92\xd0\xbe\xd0\xbf\xd1\x80\xd0\xbe\xd1\x81 \xd0\xb4\xd0\xbb\xd1\x8f \xd0\xbf\xd1\x80\xd0\xb5\xd0\xb4\xd1\x81\xd1\x82\xd0\xb0\xd0\xb2\xd0\xbb\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f \xd0\xba \xd0\xbc\xd0\xbe\xd0\xb4\xd0\xb5\xd1\x80\xd0\xb0\xd1\x86\xd0\xb8\xd0\xb8', to='lkforms.Question', unique=True)),
            ],
            options={
                'verbose_name': '\u0417\u0430\u043f\u0440\u043e\u0441 \u043d\u0430 \u043c\u043e\u0434\u0435\u0440\u0430\u0446\u0438\u044e \u0432\u043e\u043f\u0440\u043e\u0441\u0430',
                'verbose_name_plural': '\u0417\u0430\u043f\u0440\u043e\u0441\u044b \u043d\u0430 \u043c\u043e\u0434\u0435\u0440\u0430\u0446\u0438\u044e \u0432\u043e\u043f\u0440\u043e\u0441\u0430',
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='request',
            name='type',
            field=models.PositiveSmallIntegerField(default=b'0', verbose_name=b'\xd0\xa2\xd0\xb8\xd0\xbf \xd0\xb7\xd0\xb0\xd0\xbf\xd1\x80\xd0\xbe\xd1\x81\xd0\xb0', choices=[(0, b'\xd1\x83\xd0\xb4\xd0\xb0\xd0\xbb\xd0\xb8\xd1\x82\xd1\x8c'), (1, b'\xd1\x81\xd0\xbe\xd0\xb7\xd0\xb4\xd0\xb0\xd1\x82\xd1\x8c'), (2, b'\xd1\x81\xd0\xb8\xd0\xbd\xd1\x85\xd1\x80\xd0\xbe\xd0\xbd\xd0\xb8\xd0\xb7\xd0\xb8\xd1\x80\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x82\xd1\x8c \xd0\xb2\xd0\xbe\xd0\xbf\xd1\x80\xd0\xbe\xd1\x81\xd1\x8b'), (3, b'\xd1\x80\xd0\xb5\xd0\xb3\xd0\xb8\xd1\x81\xd1\x82\xd1\x80\xd0\xb0\xd1\x86\xd0\xb8\xd0\xb8 \xd0\xb2 \xd0\xb0\xd1\x80\xd1\x85\xd0\xb8\xd0\xb2'), (4, b'\xd1\x80\xd0\xb5\xd0\xb7\xd1\x83\xd0\xbb\xd1\x8c\xd1\x82\xd0\xb0\xd1\x82\xd1\x8b \xd0\xb2 \xd0\xb0\xd1\x80\xd1\x85\xd0\xb8\xd0\xb2'), (5, b'\xd1\x83\xd0\xb4\xd0\xb0\xd0\xbb\xd0\xb8\xd1\x82\xd1\x8c \xd0\xb2\xd0\xbe\xd0\xbf\xd1\x80\xd0\xbe\xd1\x81')]),
            preserve_default=True,
        ),
    ]
