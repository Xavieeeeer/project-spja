from datetime import datetime
import json

import os

import re

from urllib.parse import urlencode, urlparse

import httplib2

import urllib.request

import requests

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Platform, Game, Genre
from django.template import loader
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import *

API_URL = 'https://store.steampowered.com/api/appdetails?appids='
http = httplib2.Http()


def index(request):
    platforms = Platform.objects.all()
    games = Game.objects.all()
    """respond = requests.request(API_URL, 'GET')"""
    template = loader.get_template('index.html')
    context = {
        'latest_question_list': platforms,
        'latest_games_list': games,
    }
    return HttpResponse(template.render(context, request))


def home(request):
    games = Game.objects.all()
    template = loader.get_template('home.html')
    context = dict(latest_question_list=games)
    return HttpResponse(template.render(context, request))


def about(request):
    return render(request, 'about.html')


def account_start(request):
    respond = requests.request(API_URL, 'GET')
    template = loader.get_template('home.html')
    return HttpResponse(template.render(respond[1].decode('utf8'), request))


def games_list(request):
    result = Game.objects.all()
    for item in result:
        item.steam_price = requests.get(API_URL + str(item.steam_id)).json()[str(item.steam_id)]["data"].get("price_overview", {"final_formatted": "FREE"})["final_formatted"]
    template = loader.get_template('list_games.html')
    context = dict(games=result)
    return HttpResponse(template.render(context, request))


def detail(request, pk):
    game = get_object_or_404(Game, pk=pk)
    context = {'game': game}
    return render(request, 'game_detail.html', context)