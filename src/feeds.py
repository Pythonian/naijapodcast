from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse_lazy
from django.utils.feedgenerator import Atom1Feed, Rss201rev2Feed
from .models import Podcast, Blog


class BaseLatestBlogFeed(Feed):
    title = "Latest Blog Post Feed"
    link = '/blog/'
    description = "Stay up to date with my latest blog post on NaijaPodcast."

    def items(self):
        return Blog.objects.all()[:10]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.summary

    def item_created(self, item):
        return item.created

class AtomBlogFeed(BaseLatestBlogFeed, Feed):
    feed_type = Atom1Feed


class Rss2BlogFeed(BaseLatestBlogFeed, Feed):
    feed_type = Rss201rev2Feed


class BaseLatestPodcastFeed(Feed):
    title = "Latest Podcast Feed"
    link = '/podcasts/'
    description = "Stay up to date with my latest podcast on NaijaPodcast."

    def items(self):
        return Podcast.objects.all()[:10]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.summary

    def item_created(self, item):
        return item.created

class AtomPodcastFeed(BaseLatestPodcastFeed, Feed):
    feed_type = Atom1Feed


class Rss2PodcastFeed(BaseLatestPodcastFeed, Feed):
    feed_type = Rss201rev2Feed


