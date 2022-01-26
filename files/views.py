from django.http.response import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect
from django.views import generic
from players.models import Player, Item, File
from .forms import UploadFileForm
from files.parseFile import *


#generic way
def index(request):
    file_list = File.objects.order_by('fileDate')
    context = {'file_list': file_list}
    return render(request, 'files/index.html', context)

def uploadRaid(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            parseRaid(request, form)
            return HttpResponseRedirect('/files/')
    else:
        form = UploadFileForm()
    return render(request, 'files/uploadRaid.html', {'form': form})

def uploadGuild(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            parseGuild(request, form)
            return HttpResponseRedirect('/files/')
    else:
        form = UploadFileForm()
    return render(request, 'files/uploadGuild.html', {'form': form})

def uploadWins(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            parseWins(request, form)
            return HttpResponseRedirect('/files/')
    else:
        form = UploadFileForm()
    return render(request, 'files/uploadWins.html', {'form': form})