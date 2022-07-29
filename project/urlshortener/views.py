from audioop import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .forms import ShortenerForm
from .models import Shortener
from datetime import date


def home_view(request):
    template = 'urlshortener/home.html'
    context = {}
    context['form'] = ShortenerForm()
    if request.method == 'GET':
        return render(request, template, context)
    elif request.method == 'POST':
        used_form = ShortenerForm(request.POST)
        if used_form.is_valid():
            shortened_object = used_form.save()
            expired_date = shortened_object.expired_date
            new_url = request.build_absolute_uri('/') + shortened_object.short_url
            long_url = shortened_object.long_url
            context['expired_date'] = expired_date
            context['new_url'] = new_url
            context['long_url'] = long_url
            return render(request, template, context)
        context['errors'] = used_form.errors
        return render(request, template, context)


def today():
    pass

def redirect_url_view(request, shortened_part):
    try:
        shortener = Shortener.objects.get(short_url=shortened_part)
        shortener.times_followed += 1
        expired = shortener.expired_date<=today()
        if not expired:
            return HttpResponseRedirect(shortener.long_url)
        else:
            return HttpResponse("Link is expired")
    except:
        raise Http404('Sorry this link is broken :(')
