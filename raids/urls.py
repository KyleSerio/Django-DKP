from django.urls import path

from . import views

app_name = 'raids'
urlpatterns = [
    path('', views.index, name='index'),
    path('raidView/<str:raidDate>/', views.raidView, name='raidView'),
]