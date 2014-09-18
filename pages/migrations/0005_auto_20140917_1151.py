# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_remove_contactpage_map_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactpage',
            name='company_phone',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contactpage',
            name='company_address',
            field=wagtail.wagtailcore.fields.RichTextField(max_length=100, null=True, blank=True),
        ),
    ]
