from django.urls import path

from . import views

app_name = 'items'
urlpatterns = [
    path('', views.index, name='index'),
    path('raidView/<str:raidDate>/', views.raidView, name='raidView'),
    path('<str:itemName>/', views.detail, name='detail'),

]