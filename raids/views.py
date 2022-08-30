from django.http.response import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect
from django.views import generic
import logging
from players.models import Player, Item, File


# Create your views here.
def index(request):
    raids = Item.objects.order_by().values('itemDate').distinct().order_by('-itemDate')
    return render(request, 'raids/raidSummary.html', {'raids' : raids})

def raidView(request, raidDate):
    items = Item.objects.filter(itemDate=raidDate).order_by('-price')
    return render(request, 'raids/raidView.html', {'items' : items, 'date' : raidDate})

