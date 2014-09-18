# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_contactpage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactpage',
            old_name='latlng',
            new_name='lat_lng',
        ),
        migrations.AddField(
            model_name='contactpage',
            name='map_key',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
    ]
