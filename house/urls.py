from django.urls import path
from . import views

app_name ='house'

urlpatterns =[
    path('', views.home, name='index'),
    path('starter-page/', views.starter, name='home'),
    # path('team/', views.teams, name='team'),




]


