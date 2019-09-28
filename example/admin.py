from django.contrib import admin

# Register your models here.
from django.contrib import admin
from example.models import Movie, Genre


class MovieInLine(admin.TabularInline):
    model = Movie
    extra = 1


class GenreListAdmin(admin.ModelAdmin):
    inlines = (MovieInLine,)    #tupla, potrzebny przecinek


admin.site.register(Movie)
admin.site.register(Genre, GenreListAdmin)
