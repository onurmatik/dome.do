from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel, PageChooserPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsnippets.models import register_snippet
from modelcluster.tags import ClusterTaggableManager
from taggit.models import TaggedItemBase


# home page

class CarouselItem(Orderable):
    page = ParentalKey('pages.HomePage', related_name='carousel_items')
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    link = models.ForeignKey(
        'wagtailcore.Page',
        null=True, blank=True,
        related_name='+'
    )
    title = RichTextField()
    caption = RichTextField()
    badge = models.CharField(max_length=40, blank=True, null=True)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('title'),
        FieldPanel('caption'),
        FieldPanel('link'),
        FieldPanel('badge'),
    ]


class HomePageHighlight(Orderable):
    page = ParentalKey('pages.HomePage', related_name='homepage_highlights')
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    title = models.CharField(max_length=100)
    description = RichTextField()

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('title'),
        FieldPanel('description', classname="full"),
    ]


class HomePage(Page):
    about = RichTextField(blank=True, null=True)
    template = 'pages/home.html'

    @property
    def projects(self):
        return ProjectPage.objects.live().filter(featured=True)[:3]

    def get_context(self, request):
        context = super(HomePage, self).get_context(request)
        context['projects'] = self.projects
        return context


HomePage.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('about', classname="full"),
    InlinePanel(HomePage, 'carousel_items', label="Carousel items"),
    InlinePanel(HomePage, 'homepage_highlights', label="Highlights"),
]

HomePage.promote_panels = [
    FieldPanel('slug'),
    FieldPanel('seo_title'),
    FieldPanel('show_in_menus'),
    FieldPanel('search_description'),
]


# project pages

class ProjectListPage(Page):
    intro = RichTextField(blank=True)

    template = 'pages/project_list.html'

    @property
    def projects(self):
        return ProjectPage.objects.live()

    @property
    def tags(self):
        return set(ProjectTag.objects.values_list('tag__name', flat=True))

    def get_context(self, request):
        context = super(ProjectListPage, self).get_context(request)
        context['projects'] = self.projects
        context['tags'] = self.tags
        return context

ProjectListPage.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('intro', classname="full"),
]


class ProjectImage(models.Model):
    page = ParentalKey('pages.ProjectPage', related_name='project_images')
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    caption = models.CharField(max_length=250, blank=True, null=True)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]


class ProjectHighlight(models.Model):
    page = ParentalKey('pages.ProjectPage', related_name='project_highlights')
    highlight = RichTextField()
    type = models.PositiveSmallIntegerField(choices=((1, 'info'), (2, 'warning')),
                                            default=1)

    panels = [
        FieldPanel('highlight', classname="full"),
        FieldPanel('type'),
    ]


class ProjectTag(TaggedItemBase):
    content_object = ParentalKey('pages.ProjectPage', related_name='tagged_items')


class ProjectPage(Page):
    primary_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    description = models.TextField()
    about = RichTextField()
    video_url = models.URLField("Video embed URL", null=True, blank=True)
    tags = ClusterTaggableManager(through=ProjectTag, blank=True)
    featured = models.BooleanField(default=False, help_text='Publish on homepage')

    template = 'pages/project_detail.html'


ProjectPage.content_panels = [
    FieldPanel('title', classname="full title"),
    ImageChooserPanel('primary_image'),
    FieldPanel('description'),
    FieldPanel('tags'),
    FieldPanel('about', classname="full"),
    InlinePanel(ProjectPage, 'project_images', label="Project images"),
    InlinePanel(ProjectPage, 'project_highlights', label="Project highlights"),
    FieldPanel('video_url'),
    FieldPanel('featured'),
]

ProjectPage.promote_panels = [
    FieldPanel('slug'),
    FieldPanel('seo_title'),
    FieldPanel('show_in_menus'),
    FieldPanel('search_description'),
]


# brand snippet

class Branding(models.Model):
    logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    google = models.URLField(blank=True, null=True)

    panels = [
        ImageChooserPanel('logo'),
        FieldPanel('title'),
        FieldPanel('subtitle'),
        FieldPanel('facebook'),
        FieldPanel('twitter'),
        FieldPanel('linkedin'),
        FieldPanel('google'),
    ]

    def __unicode__(self):
        return self.title

register_snippet(Branding)


# about page

class Teaser(models.Model):
    page = ParentalKey('pages.AboutPage', related_name='teasers')
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    link = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        related_name='+'
    )

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('title'),
        FieldPanel('subtitle'),
        PageChooserPanel('link'),
    ]


class Profile(models.Model):
    page = ParentalKey('pages.AboutPage', related_name='profiles')
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    image_hover = models.ForeignKey(
        'wagtailimages.Image',
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    facebook = models.CharField(max_length=100, blank=True, null=True)
    twitter = models.CharField(max_length=100, blank=True, null=True)
    linkedin = models.CharField(max_length=100, blank=True, null=True)
    about = RichTextField()

    panels = [
        ImageChooserPanel('image'),
        ImageChooserPanel('image_hover'),
        FieldPanel('name'),
        FieldPanel('title'),
        FieldPanel('about', classname='full'),
    ]


class AboutPage(Page):
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    image_title = RichTextField(blank=True, null=True)
    image_subtitle = RichTextField(blank=True, null=True)
    intro = RichTextField()
    about = RichTextField()

    template = 'pages/about.html'


AboutPage.content_panels = [
    FieldPanel('title', classname="full title"),
    ImageChooserPanel('image'),
    FieldPanel('image_title', classname="full title"),
    FieldPanel('image_subtitle', classname="full title"),
    FieldPanel('intro'),
    FieldPanel('about', classname="full"),
    InlinePanel(AboutPage, 'teasers', label="Teasers"),
    InlinePanel(AboutPage, 'profiles', label="Team members"),
]


# contact page

class ContactPage(Page):
    intro = RichTextField()
    logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    company_name = models.CharField(max_length=100)
    company_title = models.CharField(max_length=100, blank=True, null=True)
    company_email = models.EmailField(blank=True, null=True)
    company_address = RichTextField(max_length=100, blank=True, null=True)
    company_phone = models.CharField(max_length=100, blank=True, null=True)
    lat_lng = models.CharField(max_length=100, blank=True, null=True)

    template = 'pages/contact.html'


ContactPage.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('intro'),
    ImageChooserPanel('logo'),
    FieldPanel('company_name'),
    FieldPanel('company_title'),
    FieldPanel('company_email'),
    FieldPanel('company_address'),
    FieldPanel('company_phone'),
    FieldPanel('lat_lng'),
]
