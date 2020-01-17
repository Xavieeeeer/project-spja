from django.db import models


class Platform(models.Model):
    name = models.CharField(max_length=30)


class DLC(models.Model):
    name = models.CharField(max_length=50)
    cost = models.DecimalField(decimal_places=2, max_digits=5)


class Genre(models.Model):
    name = models.CharField(max_length=40)


class Game(models.Model):
    name = models.CharField(max_length=50)
    cost = models.DecimalField(decimal_places=2, max_digits=5)
    steam_id = models.IntegerField()
    game_studio = models.CharField(max_length=40)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)


class User(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=40)


class Purchase(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField()
    proportional_price = models.DecimalField(decimal_places=2, max_digits=4)
