# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_auto_20140917_1203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branding',
            name='facebook',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='branding',
            name='google',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='branding',
            name='linkedin',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='branding',
            name='twitter',
            field=models.URLField(),
        ),
    ]
