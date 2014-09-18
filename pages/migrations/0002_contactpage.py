# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0002_initial_data'),
        ('wagtailcore', '0002_initial_data'),
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactPage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('intro', wagtail.wagtailcore.fields.RichTextField()),
                ('company_name', models.CharField(max_length=100)),
                ('company_title', models.CharField(max_length=100, null=True, blank=True)),
                ('company_email', models.EmailField(max_length=75, null=True, blank=True)),
                ('company_address', wagtail.wagtailcore.fields.RichTextField()),
                ('latlng', models.CharField(max_length=100, null=True, blank=True)),
                ('facebook', models.CharField(max_length=100, null=True, blank=True)),
                ('twitter', models.CharField(max_length=100, null=True, blank=True)),
                ('linkedin', models.CharField(max_length=100, null=True, blank=True)),
                ('logo', models.ForeignKey(related_name=b'+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='wagtailimages.Image', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
