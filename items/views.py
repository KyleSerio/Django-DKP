from django.http.response import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect
from django.views import generic
from players.models import Player, Item, File


#generic way
def index(request):
    items_list = Item.objects.order_by('itemName')
    context = {'item_list': items_list}
    return render(request, 'items/index.html', context)