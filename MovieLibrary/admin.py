from django.contrib import admin
from .models import Movie, User

# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    fields = ["title","rating"]

class UserAdmin(admin.ModelAdmin):
    fields = ["username","password"]

admin.site.register(Movie, MovieAdmin)
admin.site.register(User, UserAdmin)