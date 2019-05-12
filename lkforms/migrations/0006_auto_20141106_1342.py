# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lkforms', '0005_remove_fmqn_is_priv'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='last_reg_archivation',
            field=models.DateField(null=True, verbose_name=b'\xd0\x9f\xd0\xbe\xd1\x81\xd0\xbb\xd0\xb5\xd0\xb4\xd0\xbd\xd1\x8f\xd1\x8f \xd0\xb0\xd1\x80\xd1\x85\xd0\xb8\xd0\xb2\xd0\xb0\xd1\x86\xd0\xb8\xd1\x8f \xd1\x80\xd0\xb5\xd0\xb3\xd0\xb8\xd1\x81\xd1\x82\xd1\x80\xd0\xb0\xd1\x86\xd0\xb8\xd0\xb9'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='form',
            name='last_res_archivation',
            field=models.DateField(null=True, verbose_name=b'\xd0\x9f\xd0\xbe\xd1\x81\xd0\xbb\xd0\xb5\xd0\xb4\xd0\xbd\xd1\x8f\xd1\x8f \xd0\xb0\xd1\x80\xd1\x85\xd0\xb8\xd0\xb2\xd0\xb0\xd1\x86\xd0\xb8\xd1\x8f \xd1\x80\xd0\xb5\xd0\xb7\xd1\x83\xd0\xbb\xd1\x8c\xd1\x82\xd0\xb0\xd1\x82\xd0\xbe\xd0\xb2'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='answer',
            name='user',
            field=models.ForeignKey(related_name='answer_profile', verbose_name=b'\xd0\x9b\xd0\xbe\xd0\xb3\xd0\xb8\xd0\xbd', to='lkforms.UserProfile'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='archiveanswer',
            name='question',
            field=models.ForeignKey(related_name='archanswer_list', verbose_name=b'\xd0\x92\xd0\xbe\xd0\xbf\xd1\x80\xd0\xbe\xd1\x81', to='lkforms.Question'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='archiveanswer',
            name='user',
            field=models.ForeignKey(related_name='archanswer_profile', verbose_name=b'\xd0\x9b\xd0\xbe\xd0\xb3\xd0\xb8\xd0\xbd', to='lkforms.UserProfile'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='archiveregres',
            name='form',
            field=models.ForeignKey(related_name='archregres_list', verbose_name=b'\xd0\xa4\xd0\xbe\xd1\x80\xd0\xbc\xd0\xb0', to='lkforms.Form'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='archiveregres',
            name='user',
            field=models.ForeignKey(related_name='archregres_profile', verbose_name=b'\xd0\x9b\xd0\xbe\xd0\xb3\xd0\xb8\xd0\xbd', to='lkforms.UserProfile'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='regres',
            name='user',
            field=models.ForeignKey(related_name='regres_profile', verbose_name=b'\xd0\x9b\xd0\xbe\xd0\xb3\xd0\xb8\xd0\xbd', to='lkforms.UserProfile'),
            preserve_default=True,
        ),
    ]
