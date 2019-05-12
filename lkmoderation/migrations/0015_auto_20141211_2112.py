# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lkmoderation', '0014_auto_20141204_2016'),
    ]

    operations = [
        migrations.CreateModel(
            name='MFmMQn',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'\xd1\x81\xd0\xbe\xd0\xb7\xd0\xb4\xd0\xb0\xd0\xbd')),
                ('changed', models.DateTimeField(auto_now=True, verbose_name=b'\xd0\xb8\xd0\xb7\xd0\xbc\xd0\xb5\xd0\xbd\xd0\xb5\xd0\xbd')),
                ('number', models.CharField(default=b'', max_length=3, verbose_name=b'\xd0\x9d\xd0\xbe\xd0\xbc\xd0\xb5\xd1\x80 \xd0\xb2\xd0\xbe\xd0\xbf\xd1\x80\xd0\xbe\xd1\x81\xd0\xb0', blank=True)),
                ('form', models.ForeignKey(related_name='mfmmqn_fmlist', verbose_name=b'\xd0\xa4\xd0\xbe\xd1\x80\xd0\xbc\xd0\xb0 \xd0\xb4\xd0\xbb\xd1\x8f \xd0\xbf\xd1\x80\xd0\xb5\xd0\xb4\xd1\x81\xd1\x82\xd0\xb0\xd0\xb2\xd0\xbb\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f \xd0\xba \xd0\xbc\xd0\xbe\xd0\xb4\xd0\xb5\xd1\x80\xd0\xb0\xd1\x86\xd0\xb8\xd0\xb8', to='lkmoderation.MForm')),
                ('question', models.ForeignKey(related_name='mfmmqn_qnlist', verbose_name=b'\xd0\x92\xd0\xbe\xd0\xbf\xd1\x80\xd0\xbe\xd1\x81', to='lkmoderation.MQuestion')),
            ],
            options={
                'verbose_name': '\u041d\u0435\u043e\u0434\u043e\u0431\u0440\u0435\u043d\u043d\u044b\u0439 \u0432\u043e\u043f\u0440\u043e\u0441',
                'verbose_name_plural': '\u041d\u0435\u043e\u0434\u043e\u0431\u0440\u0435\u043d\u043d\u044b\u0435 \u0432\u043e\u043f\u0440\u043e\u0441\u044b',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MVariant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'\xd1\x81\xd0\xbe\xd0\xb7\xd0\xb4\xd0\xb0\xd0\xbd')),
                ('changed', models.DateTimeField(auto_now=True, verbose_name=b'\xd0\xb8\xd0\xb7\xd0\xbc\xd0\xb5\xd0\xbd\xd0\xb5\xd0\xbd')),
                ('name', models.CharField(max_length=250, verbose_name=b'\xd0\x92\xd0\xb0\xd1\x80\xd0\xb8\xd0\xb0\xd0\xbd\xd1\x82')),
                ('question', models.ForeignKey(related_name='variant_list', to='lkmoderation.MQuestion')),
            ],
            options={
                'verbose_name': '\u0412\u0430\u0440\u0438\u0430\u043d\u0442 \u043e\u0442\u0432\u0435\u0442\u0430',
                'verbose_name_plural': '\u0412\u0430\u0440\u0438\u0430\u043d\u0442\u044b \u043e\u0442\u0432\u0435\u0442\u0430',
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='mfmqn',
            options={'verbose_name': '\u041e\u0434\u043e\u0431\u0440\u0435\u043d\u043d\u044b\u0439 \u0432\u043e\u043f\u0440\u043e\u0441', 'verbose_name_plural': '\u041e\u0434\u043e\u0431\u0440\u0435\u043d\u043d\u044b\u0435 \u0432\u043e\u043f\u0440\u043e\u0441\u044b'},
        ),
        migrations.RemoveField(
            model_name='mquestion',
            name='form',
        ),
        migrations.RemoveField(
            model_name='mquestion',
            name='number',
        ),
        migrations.AddField(
            model_name='mquestion',
            name='comms',
            field=models.TextField(default=b'', verbose_name=b'\xd0\x9f\xd0\xbe\xd1\x8f\xd1\x81\xd0\xbd\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mquestion',
            name='multi_vars',
            field=models.BooleanField(default=False, verbose_name=b'\xd0\x9d\xd0\xb5\xd1\x81\xd0\xba\xd0\xbe\xd0\xbb\xd1\x8c\xd0\xba\xd0\xbe \xd0\xb2\xd0\xb0\xd1\x80\xd0\xb8\xd0\xb0\xd0\xbd\xd1\x82\xd0\xbe\xd0\xb2 \xd0\xbe\xd1\x82\xd0\xb2\xd0\xb5\xd1\x82\xd0\xb0'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mquestion',
            name='not_blank',
            field=models.BooleanField(default=False, verbose_name=b'\xd0\x9e\xd0\xb1\xd1\x8f\xd0\xb7\xd0\xb0\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8c\xd0\xbd\xd1\x8b\xd0\xb9'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mquestion',
            name='owner',
            field=models.ForeignKey(related_name='own_mqns', blank=True, to=settings.AUTH_USER_MODEL, help_text=b'\xd0\x92 \xd1\x81\xd0\xbf\xd0\xb8\xd1\x81\xd0\xba\xd0\xb5 \xd0\xb2\xd1\x8b\xd0\xb1\xd0\xbe\xd1\x80\xd0\xb0 \xd1\x82\xd0\xbe\xd0\xbb\xd1\x8c\xd0\xba\xd0\xbe \xd0\xbf\xd0\xbe\xd0\xbb\xd1\x8c\xd0\xb7\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x82\xd0\xb5\xd0\xbb\xd0\xb8, \xd0\xbe\xd0\xb1\xd0\xbb\xd0\xb0\xd0\xb4\xd0\xb0\xd1\x8e\xd1\x89\xd0\xb8\xd0\xb5 \xd1\x81\xd1\x82\xd0\xb0\xd1\x82\xd1\x83\xd1\x81\xd0\xbe\xd0\xbc \xd0\xbf\xd0\xb5\xd1\x80\xd1\x81\xd0\xbe\xd0\xbd\xd0\xb0\xd0\xbb\xd0\xb0 \xd0\xb8 \xd1\x81\xd0\xbe\xd1\x81\xd1\x82\xd0\xbe\xd1\x8f\xd1\x89\xd0\xb8\xd0\xb5 \xd0\xb2 \xd0\xb3\xd1\x80\xd1\x83\xd0\xbf\xd0\xbf\xd0\xb5 \xd0\x90\xd0\xb4\xd0\xbc\xd0\xb8\xd0\xbd\xd0\xb8\xd1\x81\xd1\x82\xd1\x80\xd0\xb0\xd1\x82\xd0\xbe\xd1\x80\xd1\x8b', null=True, verbose_name=b'\xd0\x92\xd0\xbb\xd0\xb0\xd0\xb4\xd0\xb5\xd0\xbb\xd0\xb5\xd1\x86'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='qrequest',
            name='question',
            field=models.ForeignKey(related_name='qreq', verbose_name=b'\xd0\x92\xd0\xbe\xd0\xbf\xd1\x80\xd0\xbe\xd1\x81 \xd0\xb4\xd0\xbb\xd1\x8f \xd0\xbf\xd1\x80\xd0\xb5\xd0\xb4\xd1\x81\xd1\x82\xd0\xb0\xd0\xb2\xd0\xbb\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f \xd0\xba \xd0\xbc\xd0\xbe\xd0\xb4\xd0\xb5\xd1\x80\xd0\xb0\xd1\x86\xd0\xb8\xd0\xb8', to='lkmoderation.MQuestion', unique=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='qrequest',
            name='type',
            field=models.PositiveSmallIntegerField(default=b'0', verbose_name=b'\xd0\xa2\xd0\xb8\xd0\xbf \xd0\xb7\xd0\xb0\xd0\xbf\xd1\x80\xd0\xbe\xd1\x81\xd0\xb0', choices=[(0, b'\xd1\x83\xd0\xb4\xd0\xb0\xd0\xbb\xd0\xb8\xd1\x82\xd1\x8c'), (1, b'\xd0\xb0\xd1\x80\xd1\x85\xd0\xb8\xd0\xb2\xd0\xb8\xd1\x80\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x82\xd1\x8c'), (2, b'\xd1\x81\xd0\xbe\xd0\xb7\xd0\xb4\xd0\xb0\xd1\x82\xd1\x8c')]),
            preserve_default=True,
        ),
    ]
