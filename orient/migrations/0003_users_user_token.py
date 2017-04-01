# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('orient', '0002_auto_20170401_1443'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='user_token',
            field=models.CharField(default=datetime.date(2017, 4, 1), max_length=250),
            preserve_default=False,
        ),
    ]
