# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dress_pool', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dress',
            options={'verbose_name': '禮服', 'verbose_name_plural': '禮服'},
        ),
        migrations.AlterModelOptions(
            name='dresstype',
            options={'verbose_name': '禮服類型', 'verbose_name_plural': '禮服類型'},
        ),
        migrations.AlterModelOptions(
            name='purpose',
            options={'verbose_name': '用途', 'verbose_name_plural': '用途'},
        ),
        migrations.AlterModelOptions(
            name='rentrecord',
            options={'verbose_name': '租借記錄', 'verbose_name_plural': '租借記錄'},
        ),
        migrations.AlterModelOptions(
            name='skirttype',
            options={'verbose_name': '裙子類型', 'verbose_name_plural': '裙子類型'},
        ),
        migrations.AddField(
            model_name='dress',
            name='remark',
            field=models.CharField(default='', verbose_name='備註 ', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dress',
            name='additional',
            field=models.IntegerField(default=0, verbose_name='禮服加價 '),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='dress',
            name='amount',
            field=models.IntegerField(default=0, verbose_name='總價 '),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='dress',
            name='color',
            field=models.CharField(verbose_name='顏色 ', max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='dress',
            name='dressType',
            field=models.ForeignKey(verbose_name='禮服類型', to='dress_pool.DressType'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='dress',
            name='image',
            field=models.ImageField(verbose_name='禮服照片 ', upload_to='pic'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='dress',
            name='number',
            field=models.CharField(verbose_name='編號 ', max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='dress',
            name='purpose',
            field=models.ForeignKey(verbose_name='用途', to='dress_pool.Purpose'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='dress',
            name='rent',
            field=models.IntegerField(default=0, verbose_name='租金 '),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='dress',
            name='skirtType',
            field=models.ForeignKey(verbose_name='裙子類型', to='dress_pool.SkirtType'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='dress',
            name='vendor',
            field=models.CharField(verbose_name='廠商 ', max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='dresstype',
            name='dressTypeName',
            field=models.CharField(verbose_name='禮服類型', max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='purpose',
            name='purposeName',
            field=models.CharField(verbose_name='用途', max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rentrecord',
            name='dress',
            field=models.ForeignKey(verbose_name='禮服', to='dress_pool.Dress'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rentrecord',
            name='rentDate',
            field=models.DateField(verbose_name='租借時間'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='skirttype',
            name='skirtTypeName',
            field=models.CharField(verbose_name='裙子類型', max_length=200),
            preserve_default=True,
        ),
    ]
