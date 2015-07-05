# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dress_pool', '0002_auto_20150704_1755'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('colorName', models.CharField(max_length=200, verbose_name='顏色')),
            ],
            options={
                'verbose_name': '顏色',
                'verbose_name_plural': '顏色',
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='dress',
            name='remark',
            field=models.CharField(max_length=200, verbose_name='備註 ', blank=True),
            preserve_default=True,
        ),
    ]
