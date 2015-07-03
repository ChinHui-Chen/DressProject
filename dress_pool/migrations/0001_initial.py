# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dress',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('vendor', models.CharField(max_length=200)),
                ('amount', models.IntegerField(default=0)),
                ('rent', models.IntegerField(default=0)),
                ('additional', models.IntegerField(default=0)),
                ('color', models.CharField(max_length=200)),
                ('number', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='pic')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DressType',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('dressTypeName', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Purpose',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('purposeName', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RentRecord',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('rentDate', models.DateField(verbose_name='date rent')),
                ('dress', models.ForeignKey(to='dress_pool.Dress')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SkirtType',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('skirtTypeName', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='dress',
            name='dressType',
            field=models.ForeignKey(to='dress_pool.DressType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dress',
            name='purpose',
            field=models.ForeignKey(to='dress_pool.Purpose'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dress',
            name='skirtType',
            field=models.ForeignKey(to='dress_pool.SkirtType'),
            preserve_default=True,
        ),
    ]
