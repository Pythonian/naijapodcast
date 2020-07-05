from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from ckeditor.fields import RichTextField
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from PIL import Image
from django.utils import timezone



# Use Abstract class ?

@python_2_unicode_compatible
class Podcast(models.Model):
	title = models.CharField(
		max_length=200,
		unique=True)
	slug = models.SlugField(
		max_length=100,
		unique=True)
	# image = ProcessedImageField(
	# 	upload_to="images",
	# 	processors = [ResizeToFill(750, 400)],
	# 	format = 'JPEG',
	# 	options = {'quality': 80, 'crop': 'Top'})
	image = models.ImageField(
		upload_to="images")
	caption = models.CharField(
		max_length=200,
		blank=True,
		help_text="Image Caption. Optional")
	summary = models.TextField()
	body = RichTextField(
		'Show Notes')
	audio_embed = models.TextField()
	created = models.DateTimeField(
        default=timezone.now)
	impressions = models.PositiveIntegerField(
        default=0,
        editable=False)

	class Meta:
		ordering = ['-created']
		get_latest_by = 'created'

	def __str__(self):
		return self.title

	def get_previous_podcast(self):
		return self.get_previous_by_created()

	def get_next_podcast(self):
		return self.get_next_by_created()

	def get_absolute_url(self):
		return reverse(
			'naijapodcast:podcast',
			kwargs={'slug': self.slug})


@python_2_unicode_compatible
class Blog(models.Model):
	title = models.CharField(
		max_length=200,
		unique=True)
	slug = models.SlugField(
		max_length=100,
		unique=True)
	image = ProcessedImageField(
		upload_to="images",
		processors = [ResizeToFill(750, 400)],
		format = 'JPEG',
		options = {'quality': 80, 'crop': 'Top'})
	caption = models.CharField(
		max_length=200,
		blank=True,
		help_text="Image Caption. Optional")
	summary = models.TextField()
	body = RichTextField()
	created = models.DateTimeField(
		default=timezone.now)
	impressions = models.PositiveIntegerField(
        default=0,
        editable=False)

	class Meta:
		ordering = ['-created']
		get_latest_by = 'created'

	def get_absolute_url(self):
		return reverse(
			'naijapodcast:blog',
			kwargs={'slug': self.slug})

	def __str__(self):
		return self.title

	def get_previous_blog(self):
		return self.get_previous_by_created()

	def get_next_blog(self):
		return self.get_next_by_created()


class PodcastImage(models.Model):
	podcast = models.ForeignKey(
		Podcast,
		blank=True,
		null=True,
		related_name='images')
	image = models.ImageField(
		upload_to='',
		blank=True,
		null=True,
	)
	caption = models.CharField(
		max_length=50,
		blank=True)
	created = models.DateTimeField(
		auto_now_add=True)


class NewsletterEmail(models.Model):
	email = models.EmailField()
	created = models.DateTimeField(
		auto_now_add=True)	

	def __unicode__(self):
		return self.email

