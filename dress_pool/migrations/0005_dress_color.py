# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dress_pool', '0004_remove_dress_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='dress',
            name='color',
            field=models.ForeignKey(default=1, to='dress_pool.Color', verbose_name='顏色'),
            preserve_default=False,
        ),
    ]
