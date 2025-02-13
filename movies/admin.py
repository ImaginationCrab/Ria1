from django.contrib import admin
from .models import Movie

# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    fields = ['id','name','price','description',]


admin.site.register(Movie, MovieAdmin)