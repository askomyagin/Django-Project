from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.template import loader
from django.shortcuts import get_object_or_404
from django.urls import reverse

def index(request):
    template = loader.get_template('TextSongs/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def performers(request):
    AllPerformers = Performers.objects.order_by('created_at')
    template = loader.get_template('TextSongs/performers.html')
    context = {'performers': AllPerformers}
    return HttpResponse(template.render(context, request))

def Perf(request, perf_name):
    artist = get_object_or_404(Performers, name=perf_name)
    albums = Albums.objects.filter(author = artist.id)
    context = {'albums': albums}
    context.update({'artist': artist})
    for album in albums:
        songs = Songs.objects.filter(album = album.id)
        context.update({album.get_title(): songs})
    template = loader.get_template('TextSongs/artist.html')
    return HttpResponse(template.render(context, request))

def song(request, song_id):
    song = get_object_or_404(Songs, id=song_id)
    template = loader.get_template('TextSongs/song.html')
    context = {'song': song}
    return HttpResponse(template.render(context, request))

def text_order(request):
    orders = OrderText.objects.order_by('-created_at')
    template = loader.get_template('TextSongs/text_order.html')
    context = {'orders': orders}
    return HttpResponse(template.render(context, request))

def create_text_order(request):
    OrderText(artist_name = request.POST['name'], album_name = request.POST['name_album'],
              song_name = request.POST['name_song'], info = request.POST['message']).save()
    return HttpResponseRedirect(reverse('textorder'))




