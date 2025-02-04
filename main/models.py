from django.db import models

# Create your models here.


# GENRE = (
#     ("Genre_1", "Genre 1",),
#     ("Genre_2", "Genre 2",),
#     ("Genre_3", "Genre 3",),
# )


class Genre(models.Model):
    name = models.CharField(max_length=256, verbose_name="Nomi")
    
    def __str__(self):
        return self.name


class Film(models.Model):
    name = models.CharField(max_length=256, verbose_name="Sarlavha")
    # genre = models.CharField(max_length=128, verbose_name="Janr", choices=GENRE)
    genre_for = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='genre_related_films')

    def __str__(self):
        return self.name
