from django.db import models

# Create your models here.
# to co chcemy odzwierciedlic w bazach danych (nasze dane do bazy danych)
from django.db import models


# tabela
class Genre(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Actor(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    date_of_birth = models.DateField()
    date_of_death = models.DateField(null=True, default=None)

    def __str__(self):
        return self.first_name, self.last_name


class Movie(models.Model):
    name = models.CharField(max_length=128)
    year = models.IntegerField()
    description = models.CharField(max_length=1024, default="")
    released = models.CharField(max_length=128)
    created_on = models.DateTimeField(auto_now_add=True)
    actors = models.ManyToManyField(Actor)
    genre = models.ForeignKey(Genre, on_delete=models.DO_NOTHING)  # moze byc CASCADE - wszytsko co poniżej też usunie
    viewed = models.BooleanField(default=False)
    is_delete = models.BooleanField(default=False)
    # rating = models.FloatField(null=True) # lub Default=0

    def __str__(self):
        return self.name

