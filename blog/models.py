from datetime import date
from django.db import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from modelcluster.fields import ParentalKey
from modelcluster.tags import ClusterTaggableManager
from taggit.models import TaggedItemBase


BLOG_CATEGORIES = (
    (1, 'Article'),
    (2, 'Application'),
    (3, 'News'),
)

class BlogIndexPage(Page):
    intro = RichTextField(blank=True)

    template = 'blog/blog_index.html'

    @property
    def posts(self):
        return BlogPage.objects.live().order_by('-date')

    @property
    def tags(self):
        return set(BlogTag.objects.values_list('tag__name', flat=True))

    def get_context(self, request):
        # Get posts
        posts = self.posts

        # Filter by tag
        tag = request.GET.get('tag')
        if tag:
            posts = posts.filter(tags__name=tag)

        # Filter by category
        cat = request.GET.get('cat')
        if cat:
            posts = posts.filter(category=cat)

        # Pagination
        page = request.GET.get('page')
        paginator = Paginator(posts, 10)  # Show 10 posts per page
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)

        # Update template context
        context = super(BlogIndexPage, self).get_context(request)
        context['posts'] = posts
        context['categories'] = BLOG_CATEGORIES
        context['selected_category'] = cat
        context['tags'] = self.tags
        context['selected_tag'] = tag
        return context

BlogIndexPage.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('intro', classname="full"),
]


# Blog page

class BlogTag(TaggedItemBase):
    content_object = ParentalKey('blog.BlogPage', related_name='tagged_items')


class BlogHighlight(models.Model):
    page = ParentalKey('blog.BlogPage', related_name='blog_highlights')
    highlight = RichTextField()

    panels = [
        FieldPanel('highlight', classname="full"),
    ]


class BlogPage(Page):
    body = RichTextField()
    teaser = RichTextField(blank=True, null=True)
    video_url = models.URLField("Video embed URL", null=True, blank=True)
    category = models.PositiveSmallIntegerField(choices=BLOG_CATEGORIES, default=1)
    tags = ClusterTaggableManager(through=BlogTag, blank=True)
    date = models.DateField("Post date")
    primary_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    author = models.ForeignKey(User, blank=True, null=True)

    template = 'blog/blog_post.html'

    @property
    def posts(self):
        return BlogPage.objects.live().exclude(id=self.id).order_by('-date')[:3]


BlogPage.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('date'),
    FieldPanel('category'),
    FieldPanel('teaser', classname="full"),
    FieldPanel('body', classname="full"),
    FieldPanel('video_url'),
    ImageChooserPanel('primary_image'),
    FieldPanel('author'),
    FieldPanel('tags'),
    InlinePanel(BlogPage, 'blog_highlights', label="Blog post highlights"),
]
