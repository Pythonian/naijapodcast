from django import template

register = template.Library()

from ..models import Podcast, Blog 
from ..forms import SearchForm 


@register.assignment_tag
def get_latest_blog():    
    return Blog.objects.all()[:2]

@register.assignment_tag
def get_popular_blog():
    return Blog.objects.order_by(
        '-impressions')[:2]

@register.assignment_tag
def get_latest_podcast():    
    return Podcast.objects.all()[:2]

@register.assignment_tag
def get_last_podcast():    
    return Podcast.objects.latest()

@register.assignment_tag
def get_popular_podcast():
    return Podcast.objects.order_by(
        '-impressions')[:2]

@register.inclusion_tag("src/_sidebar_search_box.html")
def search_box(request):
    form = SearchForm()
    return {'form': form}
