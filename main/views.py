from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
	return render(request, 'main/index.html')
