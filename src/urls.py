from django.conf.urls import url
from . import views
from django.contrib.sitemaps.views import sitemap
from django.contrib.sitemaps import GenericSitemap
from .models import Podcast, Blog 
from .feeds import AtomBlogFeed, Rss2BlogFeed, AtomPodcastFeed, Rss2PodcastFeed


info_dict = {
    'queryset': Podcast.objects.all(),
    'queryset': Blog.objects.all(),
    'date_field': 'created',
}

urlpatterns = [
    url(r'^$',
        views.home,
        name='home'),

    url(r'^about/$',
        views.about,
        name='about'),

    url(r'^search/$',
        views.search,
        name='search'),

    url(r'^host/$',
        views.host,
        name='host'),

    url(r'^terms/$',
        views.terms,
        name='terms'),

    url(r'^disclaimer/$',
        views.disclaimer,
        name='disclaimer'),

    url(r'^policy/$',
        views.policy,
        name='policy'),

    url(r'^podcasts/$',
        views.podcasts,
        name='podcasts'),

     url(r'^podcasts/rss/$', 
        Rss2PodcastFeed(),
        name='rss'),

    url(r'^podcasts/atom/$',
        AtomPodcastFeed(),
        name='atom'),

    url(r'^podcasts/(?P<slug>[\w\-]+)/$',
        views.podcast,
        name='podcast'),

    url(r'^blog/$',
        views.blogs,
        name='blogs'),

     url(r'^blog/rss/$', 
        Rss2BlogFeed(),
        name='rss'),

    url(r'^blog/atom/$',
        AtomBlogFeed(),
        name='atom'),

    url(r'^blog/(?P<slug>[\w\-]+)/$',
        views.blog,
        name='blog'),

    url(r'^contact/$',
        views.contact,
        name='contact'),

    url(r'^sitemap\.xml$', 
        sitemap,
        {'sitemaps': {'post': GenericSitemap(info_dict, priority=0.5)}},
        name='django.contrib.sitemaps.views.sitemap'),

]
