from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='dashboard-home'),
    path('matchmaking/', views.matchmaking, name='matchmaking'),
    path('matchmaking/lobby', views.lobby, name='lobby'),
    path('matchmaking/lobby/game', views.game, name='game'),
    path('profile/', views.profile, name='profile'),
    path('settings/', views.settings, name='settings'),
    path('campaign/', views.campaign, name='campaign'),
    path('customgames/', views.customgames, name='customgames'),
    path('careers/', views.careers, name='careers'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
]
