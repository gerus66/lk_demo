# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lkmoderation', '0005_auto_20141202_0538'),
    ]

    operations = [
        migrations.CreateModel(
            name='MFmMQn',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'\xd1\x81\xd0\xbe\xd0\xb7\xd0\xb4\xd0\xb0\xd0\xbd')),
                ('changed', models.DateTimeField(auto_now=True, verbose_name=b'\xd0\xb8\xd0\xb7\xd0\xbc\xd0\xb5\xd0\xbd\xd0\xb5\xd0\xbd')),
                ('number', models.CharField(max_length=3, verbose_name=b'\xd0\x9d\xd0\xbe\xd0\xbc\xd0\xb5\xd1\x80 \xd0\xb2\xd0\xbe\xd0\xbf\xd1\x80\xd0\xbe\xd1\x81\xd0\xb0', blank=True)),
                ('form', models.ForeignKey(related_name='mfmmqn_fmlist', verbose_name=b'\xd0\xa4\xd0\xbe\xd1\x80\xd0\xbc\xd0\xb0 \xd0\xb4\xd0\xbb\xd1\x8f \xd0\xbf\xd1\x80\xd0\xb5\xd0\xb4\xd1\x81\xd1\x82\xd0\xb0\xd0\xb2\xd0\xbb\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f \xd0\xba \xd0\xbc\xd0\xbe\xd0\xb4\xd0\xb5\xd1\x80\xd0\xb0\xd1\x86\xd0\xb8\xd0\xb8', to='lkmoderation.MForm')),
            ],
            options={
                'verbose_name': '\u041d\u0435\u043c\u043e\u0434\u0435\u0440\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0439 \u0432\u043e\u043f\u0440\u043e\u0441 \u0432 \u0444\u043e\u0440\u043c\u0435 \u0434\u043b\u044f \u043c\u043e\u0434\u0435\u0440\u0430\u0446\u0438\u0438',
                'verbose_name_plural': '\u041d\u0435\u043c\u043e\u0434\u0435\u0440\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0435 \u0432\u043e\u043f\u0440\u043e\u0441\u044b \u0432 \u0444\u043e\u0440\u043c\u0435 \u0434\u043b\u044f \u043c\u043e\u0434\u0435\u0440\u0430\u0446\u0438\u0438',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MQuestion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'\xd1\x81\xd0\xbe\xd0\xb7\xd0\xb4\xd0\xb0\xd0\xbd')),
                ('changed', models.DateTimeField(auto_now=True, verbose_name=b'\xd0\xb8\xd0\xb7\xd0\xbc\xd0\xb5\xd0\xbd\xd0\xb5\xd0\xbd')),
                ('name', models.CharField(max_length=250, verbose_name=b'\xd0\x92\xd0\xbe\xd0\xbf\xd1\x80\xd0\xbe\xd1\x81')),
                ('comms', models.TextField(default=b'', verbose_name=b'\xd0\x9f\xd0\xbe\xd1\x8f\xd1\x81\xd0\xbd\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f', blank=True)),
                ('not_blank', models.BooleanField(default=False, verbose_name=b'\xd0\x9e\xd0\xb1\xd1\x8f\xd0\xb7\xd0\xb0\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8c\xd0\xbd\xd1\x8b\xd0\xb9')),
                ('multi_vars', models.BooleanField(default=False, verbose_name=b'\xd0\x9d\xd0\xb5\xd1\x81\xd0\xba\xd0\xbe\xd0\xbb\xd1\x8c\xd0\xba\xd0\xbe \xd0\xb2\xd0\xb0\xd1\x80\xd0\xb8\xd0\xb0\xd0\xbd\xd1\x82\xd0\xbe\xd0\xb2 \xd0\xbe\xd1\x82\xd0\xb2\xd0\xb5\xd1\x82\xd0\xb0')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': '\u0412\u043e\u043f\u0440\u043e\u0441 \u0434\u043b\u044f \u043f\u0440\u0435\u0434\u0441\u0442\u0430\u0432\u043b\u0435\u043d\u0438\u044f \u043a \u043c\u043e\u0434\u0435\u0440\u0430\u0446\u0438\u0438',
                'verbose_name_plural': '\u0412\u043e\u043f\u0440\u043e\u0441\u044b \u0434\u043b\u044f \u043f\u0440\u0435\u0434\u0441\u0442\u0430\u0432\u043b\u0435\u043d\u0438\u044f \u043a \u043c\u043e\u0434\u0435\u0440\u0430\u0446\u0438\u0438',
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
                ('question', models.ForeignKey(related_name='mvariant_list', to='lkmoderation.MQuestion')),
            ],
            options={
                'verbose_name': '\u0412\u0430\u0440\u0438\u0430\u043d\u0442 \u043e\u0442\u0432\u0435\u0442\u0430',
                'verbose_name_plural': '\u0412\u0430\u0440\u0438\u0430\u043d\u0442\u044b \u043e\u0442\u0432\u0435\u0442\u0430',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='mfmmqn',
            name='question',
            field=models.ForeignKey(verbose_name=b'\xd0\x9d\xd0\xb5\xd0\xbc\xd0\xbe\xd0\xb4\xd0\xb5\xd1\x80\xd0\xb8\xd1\x80\xd0\xbe\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xbd\xd1\x8b\xd0\xb9 \xd0\xb2\xd0\xbe\xd0\xbf\xd1\x80\xd0\xbe\xd1\x81', to='lkmoderation.MQuestion'),
            preserve_default=True,
        ),
        migrations.AlterModelOptions(
            name='request',
            options={'verbose_name': '\u0417\u0430\u043f\u0440\u043e\u0441 \u043d\u0430 \u043c\u043e\u0434\u0435\u0440\u0430\u0446\u0438\u044e \u0444\u043e\u0440\u043c\u044b', 'verbose_name_plural': '\u0417\u0430\u043f\u0440\u043e\u0441\u044b \u043d\u0430 \u043c\u043e\u0434\u0435\u0440\u0430\u0446\u0438\u044e \u0444\u043e\u0440\u043c\u044b'},
        ),
        migrations.AlterField(
            model_name='mform',
            name='mod_pass',
            field=models.PositiveSmallIntegerField(default=b'0', verbose_name=b'\xd0\x9c\xd0\xbe\xd0\xb4\xd0\xb5\xd1\x80\xd0\xb0\xd1\x86\xd0\xb8\xd1\x8f', choices=[(0, b''), (1, b'\xd0\xbd\xd0\xb0 \xd1\x80\xd0\xb0\xd1\x81\xd1\x81\xd0\xbc\xd0\xbe\xd1\x82\xd1\x80\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb8'), (2, b'\xd0\xbe\xd0\xb4\xd0\xbe\xd0\xb1\xd1\x80\xd0\xb5\xd0\xbd\xd0\xbe'), (3, b'\xd0\xbe\xd1\x82\xd0\xba\xd0\xbb\xd0\xbe\xd0\xbd\xd0\xb5\xd0\xbd\xd0\xbe')]),
            preserve_default=True,
        ),
    ]
