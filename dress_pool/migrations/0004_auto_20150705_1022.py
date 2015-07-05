# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dress_pool', '0003_auto_20150705_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dress',
            name='color',
            field=models.ForeignKey(verbose_name='顏色', to='dress_pool.Color'),
            preserve_default=True,
        ),
    ]
