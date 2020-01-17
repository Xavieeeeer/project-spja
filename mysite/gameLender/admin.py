from django.contrib import admin
from .models import Platform, Game, Genre, User, DLC, Purchase

admin.site.register(Platform)
admin.site.register(Game)
admin.site.register(Genre)
admin.site.register(User)
admin.site.register(DLC)
admin.site.register(Purchase)
