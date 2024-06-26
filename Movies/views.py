from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Movie

def index(request):
    movies = Movie.objects.all()
    # SELECT * FROM movies_movie

    #movies = Movie.objects.filter(release_year=1985)
    # SELECT * FROM movies_movie WHERE release_year=1985

    # movies = Movie.objects.get(id=2)
    # SELECT * FROM movies_movie WHERE id=2
    # return HttpResponse(movies)

    # output = ', '.join([m.title for m in movies])
    # return HttpResponse(output)
    return render(request, 'movies/index.html', {'movies': movies})
    
def detail(request, movie_id):
    movie = get_object_or_404(Movie,pk=movie_id)
    return render (request, 'movies/detail.html', {'movie': movie})
  
   

