from django.shortcuts import render, get_object_or_404, redirect
from .models import Podcast, Blog 
from django.template.loader import get_template
from django.core.mail import EmailMessage, mail_admins
from django.template import Context
from django.contrib import messages
from .forms import ContactForm, SearchForm, NewsletterEmailForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.db import models
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.db.models import Q


PAGINATION = 10

def mk_paginator(request, items, num_items):
    '''Create and return a paginator.'''
    paginator = Paginator(items, num_items)
    try: page = int(request.GET.get('page', '1'))
    except ValueError: page = 1
    try: items = paginator.page(page)
    except (InvalidPage, EmptyPage):
        items = paginator.page(paginator.num_pages)
    return items

def home(request):
    menu = 'home'
    blogs = Blog.objects.all()[:4]
    podcasts = Podcast.objects.all()[:2]
    form = NewsletterEmailForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "You've successfully subscribed to our Newsletter. Thank you.")
        return HttpResponseRedirect(reverse('naijapodcast:home'))
    return render(
        request, 'src/home.html',
        locals())


def about(request):
    menu = 'about'
    return render(
        request, 'src/about.html',
        locals())

def host(request):
    menu = 'host'
    return render(
        request, 'src/host.html',
        locals())

def terms(request):
    return render(
        request, 'src/terms.html',
        locals())

def disclaimer(request):
    return render(
        request, 'src/disclaimer.html',
        locals())

def policy(request):
    return render(
        request, 'src/policy.html',
        locals())

def podcasts(request):
    menu = 'podcasts'
    podcasts = Podcast.objects.all()
    podcasts = mk_paginator(request, podcasts, PAGINATION)
    return render(
        request, 'src/podcasts.html',
        locals())

def podcast(request, slug):
    queryset = Podcast.objects.filter(
        slug__iexact=slug)
    if request:
        queryset.update(impressions=models.F("impressions") + 1)
    podcast = get_object_or_404(queryset)
    return render(
        request, 'src/podcast.html',
        locals())

def blogs(request):
    menu = 'blogs'
    blogs = Blog.objects.all()
    blogs = mk_paginator(request, blogs, PAGINATION) 
    return render(
        request, 'src/blogs.html',
        locals())

def blog(request, slug):
    queryset = Blog.objects.filter(
        slug__iexact=slug)
    if request:
        queryset.update(impressions=models.F("impressions") + 1)
    blog = get_object_or_404(queryset)
    return render(
        request, 'src/blog.html',
        locals())

def contact(request):
    menu = 'contact'
    form = ContactForm
    if request.method == 'POST':
        form = form(data=request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            # Email the profile with the contact info
            template = get_template('src/contact_template.txt')
            
            context = Context({
                'name': name,
                'email': email,
                'message': message,
            })
            message = template.render(context)

            email = EmailMessage(
                'New contact form submission from NaijaPodcast',
                message,
                '{} <www.naijapodcast.com>'.format(name),
                ['pythonian99@gmail.com'],
                headers={'Reply-To': email}
            )
            email.send()
            messages.success(request, "Your email has been successfully sent.")
            return HttpResponseRedirect('/contact/')

    return render(
        request, 'src/contact.html', locals())


def search(request):
    form = SearchForm()
    if request.GET.has_key('query'):
        query = request.GET['query'].strip()
        if query:
            keywords = query.split()
            q = Q()
            for keyword in keywords:
                q = q & Q(title__icontains=keyword)
            form = SearchForm({'query': query})
            podcasts = Podcast.objects.filter(q)
            blogs = Blog.objects.filter(q)
    return render(
        request,
        'src/search.html',
        locals())
