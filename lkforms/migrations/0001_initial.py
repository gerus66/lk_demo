# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'\xd1\x81\xd0\xbe\xd0\xb7\xd0\xb4\xd0\xb0\xd0\xbd')),
                ('changed', models.DateTimeField(auto_now=True, verbose_name=b'\xd0\xb8\xd0\xb7\xd0\xbc\xd0\xb5\xd0\xbd\xd0\xb5\xd0\xbd')),
                ('answer', models.CharField(default=b'', max_length=500, verbose_name=b'\xd0\x9e\xd1\x82\xd0\xb2\xd0\xb5\xd1\x82', blank=True)),
            ],
            options={
                'verbose_name': '\u041e\u0442\u0432\u0435\u0442',
                'verbose_name_plural': '\u041e\u0442\u0432\u0435\u0442\u044b',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ArchiveAnswer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'\xd1\x81\xd0\xbe\xd0\xb7\xd0\xb4\xd0\xb0\xd0\xbd')),
                ('changed', models.DateTimeField(auto_now=True, verbose_name=b'\xd0\xb8\xd0\xb7\xd0\xbc\xd0\xb5\xd0\xbd\xd0\xb5\xd0\xbd')),
                ('answer', models.CharField(default=b'', max_length=500, verbose_name=b'\xd0\x9e\xd1\x82\xd0\xb2\xd0\xb5\xd1\x82', blank=True)),
            ],
            options={
                'verbose_name': '\u041e\u0442\u0432\u0435\u0442 (\u0430\u0440\u0445\u0438\u0432)',
                'verbose_name_plural': '\u041e\u0442\u0432\u0435\u0442\u044b (\u0430\u0440\u0445\u0438\u0432)',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ArchiveRegRes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'\xd1\x81\xd0\xbe\xd0\xb7\xd0\xb4\xd0\xb0\xd0\xbd')),
                ('changed', models.DateTimeField(auto_now=True, verbose_name=b'\xd0\xb8\xd0\xb7\xd0\xbc\xd0\xb5\xd0\xbd\xd0\xb5\xd0\xbd')),
                ('is_checkin', models.BooleanField(default=False, verbose_name=b'\xd0\xa0\xd0\xb5\xd0\xb3\xd0\xb8\xd1\x81\xd1\x82\xd1\x80\xd0\xb0\xd1\x86\xd0\xb8\xd1\x8f \xd0\xbf\xd1\x80\xd0\xbe\xd0\xb9\xd0\xb4\xd0\xb5\xd0\xbd\xd0\xb0')),
                ('short_result', models.PositiveSmallIntegerField(default=0, verbose_name=b'\xd0\xa0\xd0\xb5\xd0\xb7\xd1\x83\xd0\xbb\xd1\x8c\xd1\x82\xd0\xb0\xd1\x82', choices=[(0, b'\xd0\xb2\xd1\x8b\xd0\xb1\xd1\x80\xd0\xb0\xd1\x82\xd1\x8c'), (1, b'\xd0\xb7\xd0\xb0\xd1\x87\xd0\xb5\xd1\x82'), (2, b'\xd0\xbd\xd0\xb5\xd0\xb7\xd0\xb0\xd1\x87\xd0\xb5\xd1\x82'), (3, b'\xd0\xb2 \xd1\x80\xd0\xb5\xd0\xb7\xd0\xb5\xd1\x80\xd0\xb2\xd0\xb5')])),
                ('detail_result', models.TextField(default=b'', verbose_name=b'\xd0\x94\xd0\xb5\xd1\x82\xd0\xb0\xd0\xbb\xd1\x8c\xd0\xbd\xd1\x8b\xd0\xb9 \xd1\x80\xd0\xb5\xd0\xb7\xd1\x83\xd0\xbb\xd1\x8c\xd1\x82\xd0\xb0\xd1\x82', blank=True)),
                ('private_result', models.TextField(default=b'', verbose_name=b'\xd0\xa1\xd0\xba\xd1\x80\xd1\x8b\xd1\x82\xd1\x8b\xd0\xb9 \xd1\x80\xd0\xb5\xd0\xb7\xd1\x83\xd0\xbb\xd1\x8c\xd1\x82\xd0\xb0\xd1\x82', blank=True)),
            ],
            options={
                'verbose_name': '\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u0438 \u0438 \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u044b (\u0430\u0440\u0445\u0438\u0432)',
                'verbose_name_plural': '\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u0438 \u0438 \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u044b (\u0430\u0440\u0445\u0438\u0432)',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FmQn',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'\xd1\x81\xd0\xbe\xd0\xb7\xd0\xb4\xd0\xb0\xd0\xbd')),
                ('changed', models.DateTimeField(auto_now=True, verbose_name=b'\xd0\xb8\xd0\xb7\xd0\xbc\xd0\xb5\xd0\xbd\xd0\xb5\xd0\xbd')),
                ('is_priv', models.BooleanField(default=False, verbose_name=b'\xd0\xa1\xd0\xba\xd1\x80\xd1\x8b\xd1\x82\xd1\x8b\xd0\xb9')),
            ],
            options={
                'verbose_name': '\u0412\u043e\u043f\u0440\u043e\u0441',
                'verbose_name_plural': '\u0412\u043e\u043f\u0440\u043e\u0441\u044b',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'\xd1\x81\xd0\xbe\xd0\xb7\xd0\xb4\xd0\xb0\xd0\xbd')),
                ('changed', models.DateTimeField(auto_now=True, verbose_name=b'\xd0\xb8\xd0\xb7\xd0\xbc\xd0\xb5\xd0\xbd\xd0\xb5\xd0\xbd')),
                ('full_name', models.CharField(unique=True, max_length=250, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5')),
                ('name', models.CharField(unique=True, max_length=250, verbose_name=b'\xd0\x9a\xd1\x80\xd0\xb0\xd1\x82\xd0\xba\xd0\xbe\xd0\xb5 \xd0\xbd\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5')),
                ('is_active', models.BooleanField(default=False, verbose_name=b'\xd0\xa4\xd0\xbe\xd1\x80\xd0\xbc\xd0\xb0 \xd0\xb0\xd0\xba\xd1\x82\xd0\xb8\xd0\xb2\xd0\xbd\xd0\xb0')),
                ('info', models.TextField(verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xba\xd1\x81\xd1\x82\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x8f \xd0\xb8\xd0\xbd\xd1\x84\xd0\xbe\xd1\x80\xd0\xbc\xd0\xb0\xd1\x86\xd0\xb8\xd1\x8f', blank=True)),
                ('start_time', models.DateTimeField(null=True, verbose_name=b'\xd0\x92\xd1\x80\xd0\xb5\xd0\xbc\xd1\x8f \xd0\xbd\xd0\xb0\xd1\x87\xd0\xb0\xd0\xbb\xd0\xb0', blank=True)),
                ('finish_time', models.DateTimeField(null=True, verbose_name=b'\xd0\x92\xd1\x80\xd0\xb5\xd0\xbc\xd1\x8f \xd0\xbe\xd0\xba\xd0\xbe\xd0\xbd\xd1\x87\xd0\xb0\xd0\xbd\xd0\xb8\xd1\x8f', blank=True)),
                ('file', models.FileField(upload_to=b'2', verbose_name=b'\xd0\xa4\xd0\xb0\xd0\xb9\xd0\xbb', blank=True)),
                ('result', models.FileField(help_text=b'\xd0\xa4\xd0\xb0\xd0\xb9\xd0\xbb \xd1\x81 \xd0\xbd\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5\xd0\xbc \xd0\xb2\xd0\xb8\xd0\xb4\xd0\xb0 res_[id \xd1\x84\xd0\xbe\xd1\x80\xd0\xbc\xd1\x8b]_[\xd0\xbb\xd1\x8e\xd0\xb1\xd0\xbe\xd0\xb9 \xd1\x82\xd0\xb5\xd0\xba\xd1\x81\xd1\x82].csv \xd0\xb8 \xd0\xba\xd0\xbe\xd0\xbb\xd0\xbe\xd0\xbd\xd0\xba\xd0\xb0\xd0\xbc\xd0\xb8: \xd0\xa4/\xd0\x98/\xd0\x9e/\xd0\x94.\xd1\x80./\xd0\x97\xd0\xb0\xd1\x87\xd0\xb5\xd1\x82/\xd0\xa0\xd0\xb5\xd0\xb7\xd0\xb5\xd1\x80\xd0\xb2/\xd0\x9d\xd0\xb5\xd0\xb7\xd0\xb0\xd1\x87\xd0\xb5\xd1\x82/[[Priv ]\xd0\xbb\xd1\x8e\xd0\xb1\xd0\xbe\xd0\xb9 \xd1\x82\xd0\xb5\xd0\xba\xd1\x81\xd1\x82]', upload_to=b'1', verbose_name=b'\xd0\xa0\xd0\xb5\xd0\xb7\xd1\x83\xd0\xbb\xd1\x8c\xd1\x82\xd0\xb0\xd1\x82\xd1\x8b', blank=True)),
                ('external', models.FileField(help_text=b'\xd0\xa4\xd0\xb0\xd0\xb9\xd0\xbb \xd1\x81 \xd0\xbd\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5\xd0\xbc \xd0\xb2\xd0\xb8\xd0\xb4\xd0\xb0 ext_[id \xd1\x84\xd0\xbe\xd1\x80\xd0\xbc\xd1\x8b]_[\xd0\xbb\xd1\x8e\xd0\xb1\xd0\xbe\xd0\xb9 \xd1\x82\xd0\xb5\xd0\xba\xd1\x81\xd1\x82].csv \xd0\xb8 \xd0\xba\xd0\xbe\xd0\xbb\xd0\xbe\xd0\xbd\xd0\xba\xd0\xb0\xd0\xbc\xd0\xb8: \xd0\xa4/\xd0\x98/\xd0\x9e/\xd0\x94.\xd1\x80./[id_\xd0\xb2\xd0\xbe\xd0\xbf\xd1\x80\xd0\xbe\xd1\x81\xd0\xb0].[\xd0\xbb\xd1\x8e\xd0\xb1\xd0\xbe\xd0\xb9 \xd1\x82\xd0\xb5\xd0\xba\xd1\x81\xd1\x82]', upload_to=b'1', verbose_name=b'\xd0\x94\xd0\xb0\xd0\xbd\xd0\xbd\xd1\x8b\xd0\xb5 \xd0\xb8\xd0\xb7\xd0\xb2\xd0\xbd\xd0\xb5', blank=True)),
                ('default_list', models.FileField(help_text=b'\xd0\xa4\xd0\xb0\xd0\xb9\xd0\xbb \xd1\x81 \xd0\xbd\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5\xd0\xbc \xd0\xb2\xd0\xb8\xd0\xb4\xd0\xb0 def_[id \xd1\x84\xd0\xbe\xd1\x80\xd0\xbc\xd1\x8b]_[\xd0\xbb\xd1\x8e\xd0\xb1\xd0\xbe\xd0\xb9 \xd1\x82\xd0\xb5\xd0\xba\xd1\x81\xd1\x82].csv \xd0\xb8 \xd0\xba\xd0\xbe\xd0\xbb\xd0\xbe\xd0\xbd\xd0\xba\xd0\xb0\xd0\xbc\xd0\xb8: \xd0\xa4/\xd0\x98/\xd0\x9e/\xd0\x94.\xd1\x80./[\xd0\xbb\xd1\x8e\xd0\xb1\xd0\xbe\xd0\xb9 \xd1\x82\xd0\xb5\xd0\xba\xd1\x81\xd1\x82]', upload_to=b'1', verbose_name=b'\xd0\xad\xd1\x82\xd0\xb0\xd0\xbb\xd0\xbe\xd0\xbd\xd0\xbd\xd1\x8b\xd0\xb9 \xd1\x81\xd0\xbf\xd0\xb8\xd1\x81\xd0\xbe\xd0\xba', blank=True)),
                ('aif', models.ManyToManyField(related_name='aif_set', verbose_name=b'avaliable if (OR)', to='lkforms.Form', blank=True)),
                ('aifpass', models.ManyToManyField(related_name='aifpass_set', verbose_name=b'avaliable if is_passed (OR)', to='lkforms.Form', blank=True)),
                ('aifres', models.ManyToManyField(related_name='aifres_set', verbose_name=b'avaliable if is_reserved (OR)', to='lkforms.Form', blank=True)),
                ('unaif', models.ManyToManyField(related_name='unaif_set', verbose_name=b'unavaliable if (OR)', to='lkforms.Form', blank=True)),
            ],
            options={
                'verbose_name': '\u0424\u043e\u0440\u043c\u0430 \u0441 \u0432\u043e\u043f\u0440\u043e\u0441\u0430\u043c\u0438',
                'verbose_name_plural': '\u0424\u043e\u0440\u043c\u044b \u0441 \u0432\u043e\u043f\u0440\u043e\u0441\u0430\u043c\u0438',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'\xd1\x81\xd0\xbe\xd0\xb7\xd0\xb4\xd0\xb0\xd0\xbd')),
                ('changed', models.DateTimeField(auto_now=True, verbose_name=b'\xd0\xb8\xd0\xb7\xd0\xbc\xd0\xb5\xd0\xbd\xd0\xb5\xd0\xbd')),
                ('name', models.CharField(max_length=250, verbose_name=b'\xd0\x92\xd0\xbe\xd0\xbf\xd1\x80\xd0\xbe\xd1\x81')),
                ('comms', models.TextField(verbose_name=b'\xd0\x9f\xd0\xbe\xd1\x8f\xd1\x81\xd0\xbd\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f', blank=True)),
                ('not_blank', models.BooleanField(default=False, verbose_name=b'\xd0\x9e\xd0\xb1\xd1\x8f\xd0\xb7\xd0\xb0\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8c\xd0\xbd\xd1\x8b\xd0\xb9')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': '\u0412\u043e\u043f\u0440\u043e\u0441',
                'verbose_name_plural': '\u0412\u043e\u043f\u0440\u043e\u0441\u044b',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RegRes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'\xd1\x81\xd0\xbe\xd0\xb7\xd0\xb4\xd0\xb0\xd0\xbd')),
                ('changed', models.DateTimeField(auto_now=True, verbose_name=b'\xd0\xb8\xd0\xb7\xd0\xbc\xd0\xb5\xd0\xbd\xd0\xb5\xd0\xbd')),
                ('is_checkin', models.BooleanField(default=False, verbose_name=b'\xd0\xa0\xd0\xb5\xd0\xb3\xd0\xb8\xd1\x81\xd1\x82\xd1\x80\xd0\xb0\xd1\x86\xd0\xb8\xd1\x8f \xd0\xbf\xd1\x80\xd0\xbe\xd0\xb9\xd0\xb4\xd0\xb5\xd0\xbd\xd0\xb0')),
                ('short_result', models.PositiveSmallIntegerField(default=0, verbose_name=b'\xd0\xa0\xd0\xb5\xd0\xb7\xd1\x83\xd0\xbb\xd1\x8c\xd1\x82\xd0\xb0\xd1\x82', choices=[(0, b'\xd0\xb2\xd1\x8b\xd0\xb1\xd1\x80\xd0\xb0\xd1\x82\xd1\x8c'), (1, b'\xd0\xb7\xd0\xb0\xd1\x87\xd0\xb5\xd1\x82'), (2, b'\xd0\xbd\xd0\xb5\xd0\xb7\xd0\xb0\xd1\x87\xd0\xb5\xd1\x82'), (3, b'\xd0\xb2 \xd1\x80\xd0\xb5\xd0\xb7\xd0\xb5\xd1\x80\xd0\xb2\xd0\xb5')])),
                ('detail_result', models.TextField(default=b'', verbose_name=b'\xd0\x94\xd0\xb5\xd1\x82\xd0\xb0\xd0\xbb\xd1\x8c\xd0\xbd\xd1\x8b\xd0\xb9 \xd1\x80\xd0\xb5\xd0\xb7\xd1\x83\xd0\xbb\xd1\x8c\xd1\x82\xd0\xb0\xd1\x82', blank=True)),
                ('private_result', models.TextField(default=b'', verbose_name=b'\xd0\xa1\xd0\xba\xd1\x80\xd1\x8b\xd1\x82\xd1\x8b\xd0\xb9 \xd1\x80\xd0\xb5\xd0\xb7\xd1\x83\xd0\xbb\xd1\x8c\xd1\x82\xd0\xb0\xd1\x82', blank=True)),
                ('form', models.ForeignKey(related_name='regres_list', verbose_name=b'\xd0\xa4\xd0\xbe\xd1\x80\xd0\xbc\xd0\xb0', to='lkforms.Form')),
            ],
            options={
                'verbose_name': '\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u0438 \u0438 \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u044b',
                'verbose_name_plural': '\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u0438 \u0438 \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u044b',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'\xd1\x81\xd0\xbe\xd0\xb7\xd0\xb4\xd0\xb0\xd0\xbd')),
                ('changed', models.DateTimeField(auto_now=True, verbose_name=b'\xd0\xb8\xd0\xb7\xd0\xbc\xd0\xb5\xd0\xbd\xd0\xb5\xd0\xbd')),
                ('sname', models.CharField(max_length=50, verbose_name=b'\xd0\xa4\xd0\xb0\xd0\xbc\xd0\xb8\xd0\xbb\xd0\xb8\xd1\x8f')),
                ('name', models.CharField(max_length=50, verbose_name=b'\xd0\x98\xd0\xbc\xd1\x8f')),
                ('pname', models.CharField(max_length=50, verbose_name=b'\xd0\x9e\xd1\x82\xd1\x87\xd0\xb5\xd1\x81\xd1\x82\xd0\xb2\xd0\xbe')),
                ('sex', models.PositiveSmallIntegerField(default=b'0', verbose_name=b'\xd0\x9f\xd0\xbe\xd0\xbb', choices=[(0, b'\xd0\xb2\xd1\x8b\xd0\xb1\xd1\x80\xd0\xb0\xd1\x82\xd1\x8c'), (1, b'\xd0\xb6\xd0\xb5\xd0\xbd'), (2, b'\xd0\xbc\xd1\x83\xd0\xb6')])),
                ('bday', models.DateField(verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd1\x80\xd0\xbe\xd0\xb6\xd0\xb4\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f')),
                ('src', models.PositiveSmallIntegerField(default=b'0', verbose_name=b'\xd0\x98\xd1\x81\xd1\x82\xd0\xbe\xd1\x87\xd0\xbd\xd0\xb8\xd0\xba', choices=[(0, b'\xd0\xb2\xd1\x8b\xd0\xb1\xd1\x80\xd0\xb0\xd1\x82\xd1\x8c'), (1, b'\xd0\xb8\xd0\xbd\xd1\x82\xd0\xb5\xd1\x80\xd0\xbd\xd0\xb5\xd1\x82'), (2, b'\xd1\x83\xd1\x87\xd0\xb8\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8c'), (3, b'\xd0\xb7\xd0\xbd\xd0\xb0\xd0\xba\xd0\xbe\xd0\xbc\xd1\x8b\xd0\xb9'), (4, b'email \xd0\xbf\xd0\xb8\xd1\x81\xd1\x8c\xd0\xbc\xd0\xbe'), (5, b'\xd0\xb6\xd1\x83\xd1\x80\xd0\xbd\xd0\xb0\xd0\xbb "\xd0\x9a\xd0\xb2\xd0\xb0\xd0\xbd\xd1\x82"'), (6, b'\xd0\xb6\xd1\x83\xd1\x80\xd0\xbd\xd0\xb0\xd0\xbb "\xd0\x9f\xd0\xbe\xd1\x82\xd0\xb5\xd0\xbd\xd1\x86\xd0\xb8\xd0\xb0\xd0\xbb"'), (7, b'\xd0\x92\xd0\x97\xd0\x9c\xd0\xa8'), (8, b'\xd0\xb4\xd1\x80\xd1\x83\xd0\xb3\xd0\xbe\xd0\xb5')])),
                ('yasrc', models.CharField(max_length=500, verbose_name=b'\xd0\x94\xd1\x80\xd1\x83\xd0\xb3\xd0\xbe\xd0\xb5', blank=True)),
                ('user', models.ForeignKey(related_name='profile', verbose_name=b'\xd0\x9b\xd0\xbe\xd0\xb3\xd0\xb8\xd0\xbd', to=settings.AUTH_USER_MODEL, unique=True)),
            ],
            options={
                'verbose_name': '\u041f\u0440\u043e\u0444\u0438\u043b\u044c \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f',
                'verbose_name_plural': '\u041f\u0440\u043e\u0444\u0438\u043b\u0438 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0435\u0439',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Variant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'\xd1\x81\xd0\xbe\xd0\xb7\xd0\xb4\xd0\xb0\xd0\xbd')),
                ('changed', models.DateTimeField(auto_now=True, verbose_name=b'\xd0\xb8\xd0\xb7\xd0\xbc\xd0\xb5\xd0\xbd\xd0\xb5\xd0\xbd')),
                ('name', models.CharField(max_length=250, verbose_name=b'\xd0\x92\xd0\xb0\xd1\x80\xd0\xb8\xd0\xb0\xd0\xbd\xd1\x82')),
                ('question', models.ForeignKey(to='lkforms.Question')),
            ],
            options={
                'verbose_name': '\u0412\u0430\u0440\u0438\u0430\u043d\u0442 \u043e\u0442\u0432\u0435\u0442\u0430',
                'verbose_name_plural': '\u0412\u0430\u0440\u0438\u0430\u043d\u0442\u044b \u043e\u0442\u0432\u0435\u0442\u0430',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='regres',
            name='user',
            field=models.ForeignKey(verbose_name=b'\xd0\x9b\xd0\xbe\xd0\xb3\xd0\xb8\xd0\xbd', to='lkforms.UserProfile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fmqn',
            name='form',
            field=models.ForeignKey(related_name='fmqn_fmlist', verbose_name=b'\xd0\xa4\xd0\xbe\xd1\x80\xd0\xbc\xd0\xb0 \xd1\x81 \xd0\xb2\xd0\xbe\xd0\xbf\xd1\x80\xd0\xbe\xd1\x81\xd0\xb0\xd0\xbc\xd0\xb8', to='lkforms.Form'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fmqn',
            name='question',
            field=models.ForeignKey(verbose_name=b'\xd0\x92\xd0\xbe\xd0\xbf\xd1\x80\xd0\xbe\xd1\x81', to='lkforms.Question'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='archiveregres',
            name='form',
            field=models.ForeignKey(verbose_name=b'\xd0\xa4\xd0\xbe\xd1\x80\xd0\xbc\xd0\xb0', to='lkforms.Form'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='archiveregres',
            name='user',
            field=models.ForeignKey(verbose_name=b'\xd0\x9b\xd0\xbe\xd0\xb3\xd0\xb8\xd0\xbd', to='lkforms.UserProfile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='archiveanswer',
            name='question',
            field=models.ForeignKey(verbose_name=b'\xd0\x92\xd0\xbe\xd0\xbf\xd1\x80\xd0\xbe\xd1\x81', to='lkforms.Question'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='archiveanswer',
            name='user',
            field=models.ForeignKey(verbose_name=b'\xd0\x9b\xd0\xbe\xd0\xb3\xd0\xb8\xd0\xbd', to='lkforms.UserProfile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(related_name='answer_list', verbose_name=b'\xd0\x92\xd0\xbe\xd0\xbf\xd1\x80\xd0\xbe\xd1\x81', to='lkforms.Question'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='answer',
            name='user',
            field=models.ForeignKey(verbose_name=b'\xd0\x9b\xd0\xbe\xd0\xb3\xd0\xb8\xd0\xbd', to='lkforms.UserProfile'),
            preserve_default=True,
        ),
    ]
