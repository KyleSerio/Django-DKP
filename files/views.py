from django.http.response import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect
from django.views import generic
from players.models import Player, Item, File
from .forms import UploadFileForm
from files.parseFile import *


#Landing page, displays upload file option. File List not used(yet?)
def index(request):
    file_list = File.objects.order_by('fileDate')
    context = {'file_list': file_list}
    return render(request, 'files/index.html', context)

#Gives the user the option to upload different log types, and parse them accordingly.
def uploadFile(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            type = form.cleaned_data.get("type")
            #type corresponds to the 1st part of the logTypes tuple in forms
            context = []
            if type[0] == "1": #
                parseGuild(request, form)
            elif type[0] == "2":
                parseRaid(request, form)
            elif type[0] == "3":
                winsList = parseWins(request, form)
                context = {'winsList': winsList}
            return render(request, 'files/confirm.html', context)
    else:
        form = UploadFileForm()
    return render(request, 'files/uploadFile.html', {'form': form})

def confirm(request):
    return render(request, 'files/confirm.html')