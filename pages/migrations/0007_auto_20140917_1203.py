# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_contactpage_google'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactpage',
            name='facebook',
        ),
        migrations.RemoveField(
            model_name='contactpage',
            name='google',
        ),
        migrations.RemoveField(
            model_name='contactpage',
            name='linkedin',
        ),
        migrations.RemoveField(
            model_name='contactpage',
            name='twitter',
        ),
        migrations.AddField(
            model_name='branding',
            name='facebook',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='branding',
            name='google',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='branding',
            name='linkedin',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='branding',
            name='twitter',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
    ]
