from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('games/', views.account_start, name='account_start'),
    path('list/', views.games_list, name='list_games'),
    re_path(r'detail/(?P<pk>\d+)/$', views.detail, name='game_detail'),

]
