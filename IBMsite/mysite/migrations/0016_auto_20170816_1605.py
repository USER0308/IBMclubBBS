# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-16 16:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0015_auto_20170816_1052'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment_Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('floor', models.IntegerField(default=2)),
                ('author', models.CharField(default=b'NoBody', max_length=20)),
                ('content', models.CharField(max_length=10240)),
                ('time', models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'\xe5\x8f\x91\xe8\xa1\xa8\xe6\x97\xb6\xe9\x97\xb4')),
                ('parent_floor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mysite.Comment_Model')),
                ('ref_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.Post_Model')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='comment_model',
            unique_together=set([('ref_post', 'floor')]),
        ),
    ]
