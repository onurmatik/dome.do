# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import modelcluster.fields
import wagtail.wagtailcore.fields
from django.conf import settings
import modelcluster.tags


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0002_initial_data'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wagtailcore', '0002_initial_data'),
        ('taggit', '0002_auto_20140914_1805'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogHighlight',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('highlight', wagtail.wagtailcore.fields.RichTextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BlogIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('intro', wagtail.wagtailcore.fields.RichTextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='BlogPage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('body', wagtail.wagtailcore.fields.RichTextField()),
                ('teaser', wagtail.wagtailcore.fields.RichTextField(null=True, blank=True)),
                ('video_url', models.URLField(null=True, verbose_name=b'Video embed URL', blank=True)),
                ('category', models.PositiveSmallIntegerField(default=1, choices=[(1, b'Article'), (2, b'Application'), (3, b'News')])),
                ('date', models.DateField(verbose_name=b'Post date')),
                ('author', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('primary_image', models.ForeignKey(related_name=b'+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='wagtailimages.Image', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='BlogTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content_object', modelcluster.fields.ParentalKey(related_name=b'tagged_items', to='blog.BlogPage')),
                ('tag', models.ForeignKey(related_name='blog_blogtag_items', to='taggit.Tag')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='blogpage',
            name='tags',
            field=modelcluster.tags.ClusterTaggableManager(to='taggit.Tag', through='blog.BlogTag', blank=True, help_text='A comma-separated list of tags.', verbose_name='Tags'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bloghighlight',
            name='page',
            field=modelcluster.fields.ParentalKey(related_name=b'blog_highlights', to='blog.BlogPage'),
            preserve_default=True,
        ),
    ]
