from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Album, Song
from django.template import loader
#import psutil
import os

def index(request):
	all_albums = Album.objects.all()
	context = {'all_albums': all_albums,}
	return render(request, 'music/index.html', context)

def detail(request, album_id):
	album = get_object_or_404(Album, pk=album_id)
	return render(request, 'music/detail.html', {'album':album})

def play(request, album_id, song):
	album = get_object_or_404(Album, pk=album_id)
#	for proc in psutil.process_iter():
#    		if proc.name() == 'mpg321':
#			print('\n\n\n\n\n', proc)
#			os.system('kill ' + str(proc.pid))
#	os.system('mpg321 "music/songs/' + album.album_title + '/' + song + '.mp3" &')
	return render(request, 'music/detail.html', {'album':album})

def stop(request, album_id):
#	for proc in psutil.process_iter():
#    		if proc.name() == 'mpg321':
#			os.system('kill ' + str(proc.pid))
	album = get_object_or_404(Album, pk=album_id)
	return render(request, 'music/detail.html', {'album':album})




