from django.contrib import admin
from django.db.models import Count
from .models import Genre, Movie

class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'count_movies')

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(_count_movies=Count("movie"))  # Annotate the count of movies
        return queryset

    def count_movies(self, obj):
        return obj._count_movies
    count_movies.admin_order_field = '_count_movies'  # Make count_movies sortable
    count_movies.short_description = 'Count Movies'

class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'release_year', 'number_in_stock', 'daily_rate', 'genre', 'date_created')
    exclude = ('date_created',)
    search_fields = ['title', 'release_year']
    list_filter = ('genre',)

# Register your models here.

admin.site.site_header = "Vidly Administration"
admin.site.site_title = "Vidly Administration"
admin.site.index_title = "Welcome to Vidly Administration"    

admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)