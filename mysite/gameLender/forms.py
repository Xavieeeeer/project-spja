from django import forms
from django.contrib.contenttypes import fields
from django.core.exceptions import ValidationError
from .models import Game


class GameForm(forms.ModelForm):
    class meta:
        model = Game
        fields = ['name', 'cost', 'game_studio', 'genre']


class SearchGameForm(forms.ModelForm):
    from_price = forms.IntegerField(label='from')
    to_price = forms.IntegerField(label='to')
