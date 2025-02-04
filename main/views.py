from django.views.generic import ListView
from django.db.models import Q
from .models import Film

# Create your views here.


class IndexPage(ListView):
    model = Film
    template_name = "index.html"


class SearchPage(ListView):
    model = Film
    template_name = "search.html"

    def get_queryset(self):
        return super().get_queryset().filter(
            Q(name__icontains=self.request.GET.get('q')) | Q(genre_for__name__icontains=self.request.GET.get('q'))
        )


class GenrePage(ListView):
    model = Film
    template_name = "genre.html"

    def get_queryset(self):
        return super().get_queryset().filter(genre_for__id=self.kwargs.get('genre'))
