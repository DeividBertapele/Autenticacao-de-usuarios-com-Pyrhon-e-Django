from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sigup/', views.sigup, name='sigup'),
    path('sigin/', views.sigin, name='sigin'),
    path('sair/', views.sair, name='sair'),
    path('tasks/', views.tasks, name='tasks'),

]