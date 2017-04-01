# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orient', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='main',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('profile', models.CharField(max_length=250, null=True)),
                ('teamid', models.CharField(max_length=250, null=True)),
                ('user_id', models.ForeignKey(to='orient.Users', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameField(
            model_name='users',
            old_name='idn',
            new_name='user_id',
        ),
        migrations.AddField(
            model_name='data',
            name='user_id',
            field=models.ForeignKey(to='orient.Users', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='data',
            name='idn',
            field=models.CharField(max_length=250),
        ),
    ]
