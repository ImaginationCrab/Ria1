from django.contrib import admin
from .models import Movie, User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    fields = ["username","password"]

admin.site.register(Movie)
admin.site.register(User, UserAdmin)