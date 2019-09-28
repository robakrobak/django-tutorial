from django.shortcuts import render

# Create your views here.
# cos co reprezentuje dane, aby były zrozumiałem dla frontendu

from django.http import HttpResponse
from django.shortcuts import render, reverse
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from example.models import Movie, Genre
from example.forms import MovieForm, GenreForm


def hello_world(request):  # przyjmuje wartości z przeglądarki, metadane itp.
    return HttpResponse('Hello World! Mam dwa koty i chciałbym mieć wiewiórkę rudo-niebieską.')


def hello_name(request, name):
    return HttpResponse(f"Hello {name}!")


def hello_world_template(request):
    return render(request, "index.html", {})


def simple_list_view(request):
    movies_query = Movie.objects.all()
    return render(request, "list.html", {"movies": movies_query})


class MovieListView(ListView):
    model = Movie
    template_name = "list.html"
    context_object_name = "movies"


class GenreListView(ListView):
    model = Genre
    template_name = "list.html"
    context_object_name = "movies"


class PostCreateView(CreateView):
    model = Movie
    form_class = MovieForm
    success_url = "/movie/add"
    template_name = "add.html"


class PostEditView(UpdateView):
    model = Movie
    form_class = MovieForm
    template_name = "add.html"

    @property
    def success_url(self):
        return reverse("movie_list")


class GenreCreateView(CreateView):
    model = Genre
    form_class = GenreForm
    success_url = "/genre/add"
    template_name = "add.html"


class GenreEditView(UpdateView):
    model = Genre
    form_class = GenreForm
    template_name = "add.html"

    @property
    def success_url(self):
        return reverse("movie_list")


class PostDeleteView(DeleteView):  #obejrzyj sobie list HTML
    model = Movie
    template_name = "delete.html"

    @property
    def success_url(self):
        return reverse("movie_list")


