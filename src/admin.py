from django.contrib import admin
from .models import Podcast, Blog, PodcastImage, NewsletterEmail


class PodcastImageInline(admin.StackedInline):
	model = PodcastImage
	extra = 0

@admin.register(Podcast)
class PodcastAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',)}
	list_display = ['title', 'created']
	date_hierarchy = 'created'
	search_fields = ['title']
	list_filter = ['created']
	inlines = [PodcastImageInline]


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',)}
	list_display = ['title', 'created']
	date_hierarchy = 'created'
	search_fields = ['title']
	list_filter = ['created']


admin.site.register(NewsletterEmail)

