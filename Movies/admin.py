from django.contrib import admin
from .models import Genre, Movie

class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'release_year', 'number_in_stock', 'daily_rate', 'genre', 'date_created')
    exclude = ('date_created',)

# Register your models here.



admin.site.site_header = "Vidly Administration"
admin.site.site_title = "Vidly Administration"
admin.site.index_title = "Welcome to Vidly Administration"    

admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)

