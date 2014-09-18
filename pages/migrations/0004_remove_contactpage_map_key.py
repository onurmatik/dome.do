# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20140917_1049'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactpage',
            name='map_key',
        ),
    ]
