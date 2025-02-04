from django.urls import path
from .views import IndexPage, SearchPage, GenrePage


urlpatterns = [
    path('', IndexPage.as_view(), name='index_page'),
    path('search', SearchPage.as_view(), name='search_page'),
    path('genre/<int:genre>/', GenrePage.as_view(), name='genre_page'),
]
