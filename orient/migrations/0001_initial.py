# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='data',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=100, null=True)),
                ('last_name', models.CharField(max_length=1000, null=True)),
                ('headline', models.CharField(max_length=1000, null=True)),
                ('location', models.CharField(max_length=10000, null=True)),
                ('summary', models.CharField(max_length=1000, null=True)),
                ('tags', models.CharField(max_length=1000, null=True)),
                ('state', models.IntegerField(max_length=250, null=True, blank=True)),
                ('picture_url', models.CharField(max_length=250, null=True)),
                ('public_profile_url', models.CharField(max_length=11250, null=True)),
                ('email_address', models.CharField(max_length=250, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Saved',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('saved_id', models.CharField(max_length=250)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('idn', models.CharField(max_length=250)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='saved',
            name='idn',
            field=models.ForeignKey(to='orient.Users'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='data',
            name='idn',
            field=models.ForeignKey(to='orient.Users', null=True),
            preserve_default=True,
        ),
    ]
