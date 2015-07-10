# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import dress_pool.models


class Migration(migrations.Migration):

    dependencies = [
        ('dress_pool', '0005_dress_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dress',
            name='image',
            field=models.ImageField(validators=[dress_pool.models.Dress.validate_image], upload_to='pic', verbose_name='禮服照片 '),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='dress',
            name='vendor',
            field=models.CharField(verbose_name='廠商 ', max_length=200, blank=True),
            preserve_default=True,
        ),
    ]
