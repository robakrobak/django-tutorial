from django.db import models

# Create your models here.
# to co chcemy odzwierciedlic w bazach danych (nasze dane do bazy danych)
from django.db import models


# tabela
class Genre(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=128)
    year = models.IntegerField()
    released = models.CharField(max_length=128)
    created_on = models.DateTimeField(auto_now_add=True)
    genre = models.ForeignKey(Genre, on_delete=models.DO_NOTHING)  # moze byc CASCADE - wszytsko co poniżej też usunie
    viewed = models.BooleanField(default=False)
    is_delete = models.BooleanField(default=False)
    # rating = models.FloatField(null=True) # lub Default=0

    def __str__(self):
        return self.name
