from django.urls import path

from . import views

app_name = 'files'
urlpatterns = [
    path('', views.index, name='index'),
    path('uploadRaid', views.uploadRaid, name='uploadRaid'),
    path('uploadGuild', views.uploadGuild, name='uploadGuild'),
    path('uploadWins', views.uploadWins, name='uploadWins'),

]