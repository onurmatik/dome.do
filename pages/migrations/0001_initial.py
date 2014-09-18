# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import modelcluster.fields
import wagtail.wagtailcore.fields
import modelcluster.tags


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0002_initial_data'),
        ('wagtailcore', '0002_initial_data'),
        ('taggit', '0002_auto_20140914_1805'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutPage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('image_title', wagtail.wagtailcore.fields.RichTextField(null=True, blank=True)),
                ('image_subtitle', wagtail.wagtailcore.fields.RichTextField(null=True, blank=True)),
                ('intro', wagtail.wagtailcore.fields.RichTextField()),
                ('about', wagtail.wagtailcore.fields.RichTextField()),
                ('image', models.ForeignKey(related_name=b'+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='wagtailimages.Image', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='Branding',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('subtitle', models.CharField(max_length=100)),
                ('facebook', models.URLField(null=True, blank=True)),
                ('twitter', models.URLField(null=True, blank=True)),
                ('linkedin', models.URLField(null=True, blank=True)),
                ('google', models.URLField(null=True, blank=True)),
                ('logo', models.ForeignKey(related_name=b'+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='wagtailimages.Image', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CarouselItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sort_order', models.IntegerField(null=True, editable=False, blank=True)),
                ('title', wagtail.wagtailcore.fields.RichTextField()),
                ('caption', wagtail.wagtailcore.fields.RichTextField()),
                ('badge', models.CharField(max_length=40, null=True, blank=True)),
                ('image', models.ForeignKey(related_name=b'+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='wagtailimages.Image', null=True)),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ContactPage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('intro', wagtail.wagtailcore.fields.RichTextField()),
                ('company_name', models.CharField(max_length=100)),
                ('company_title', models.CharField(max_length=100, null=True, blank=True)),
                ('company_email', models.EmailField(max_length=75, null=True, blank=True)),
                ('company_address', wagtail.wagtailcore.fields.RichTextField(max_length=100, null=True, blank=True)),
                ('company_phone', models.CharField(max_length=100, null=True, blank=True)),
                ('lat_lng', models.CharField(max_length=100, null=True, blank=True)),
                ('logo', models.ForeignKey(related_name=b'+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='wagtailimages.Image', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('about', wagtail.wagtailcore.fields.RichTextField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='HomePageHighlight',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sort_order', models.IntegerField(null=True, editable=False, blank=True)),
                ('title', models.CharField(max_length=100)),
                ('description', wagtail.wagtailcore.fields.RichTextField()),
                ('image', models.ForeignKey(related_name=b'+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='wagtailimages.Image', null=True)),
                ('page', modelcluster.fields.ParentalKey(related_name=b'homepage_highlights', to='pages.HomePage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('facebook', models.CharField(max_length=100, null=True, blank=True)),
                ('twitter', models.CharField(max_length=100, null=True, blank=True)),
                ('linkedin', models.CharField(max_length=100, null=True, blank=True)),
                ('about', wagtail.wagtailcore.fields.RichTextField()),
                ('image', models.ForeignKey(related_name=b'+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='wagtailimages.Image', null=True)),
                ('image_hover', models.ForeignKey(related_name=b'+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='wagtailimages.Image', null=True)),
                ('page', modelcluster.fields.ParentalKey(related_name=b'profiles', to='pages.AboutPage')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProjectHighlight',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('highlight', wagtail.wagtailcore.fields.RichTextField()),
                ('type', models.PositiveSmallIntegerField(default=1, choices=[(1, b'info'), (2, b'warning')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProjectImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('caption', models.CharField(max_length=250, null=True, blank=True)),
                ('image', models.ForeignKey(related_name=b'+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='wagtailimages.Image', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProjectListPage',
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
            name='ProjectPage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('description', models.TextField()),
                ('about', wagtail.wagtailcore.fields.RichTextField()),
                ('video_url', models.URLField(null=True, verbose_name=b'Video embed URL', blank=True)),
                ('featured', models.BooleanField(default=False, help_text=b'Publish on homepage')),
                ('primary_image', models.ForeignKey(related_name=b'+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='wagtailimages.Image', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='ProjectTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content_object', modelcluster.fields.ParentalKey(related_name=b'tagged_items', to='pages.ProjectPage')),
                ('tag', models.ForeignKey(related_name='pages_projecttag_items', to='taggit.Tag')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Teaser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('subtitle', models.CharField(max_length=100)),
                ('image', models.ForeignKey(related_name=b'+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='wagtailimages.Image', null=True)),
                ('link', models.ForeignKey(related_name=b'+', blank=True, to='wagtailcore.Page', null=True)),
                ('page', modelcluster.fields.ParentalKey(related_name=b'teasers', to='pages.AboutPage')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='projectpage',
            name='tags',
            field=modelcluster.tags.ClusterTaggableManager(to='taggit.Tag', through='pages.ProjectTag', blank=True, help_text='A comma-separated list of tags.', verbose_name='Tags'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='projectimage',
            name='page',
            field=modelcluster.fields.ParentalKey(related_name=b'project_images', to='pages.ProjectPage'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='projecthighlight',
            name='page',
            field=modelcluster.fields.ParentalKey(related_name=b'project_highlights', to='pages.ProjectPage'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='carouselitem',
            name='link',
            field=models.ForeignKey(related_name=b'+', blank=True, to='wagtailcore.Page', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='carouselitem',
            name='page',
            field=modelcluster.fields.ParentalKey(related_name=b'carousel_items', to='pages.HomePage'),
            preserve_default=True,
        ),
    ]
