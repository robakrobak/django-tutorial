from rest_framework import serializers

from example.models import Movie, Genre, Actor


class GenreSerializer(serializers.ModelSerializer):
    """
    Serializing all the Genre
    """

    class Meta:
        model = Genre
        fields = ("id", "name")


class MovieSerializer(serializers.ModelSerializer):
    """
    Serializing all the Movies
    """

    # genre = GenreSerializer()    #

    class Meta:
        model = Movie
        fields = ("id", "name", "description", "year", "released", "actors", "genre", "viewed", "is_delete")


class MovieMiniSerializer(serializers.ModelSerializer):
    """
    Serializing all the Movies
    """

    class Meta:
        model = Movie
        fields = ("id", "name")

class ActorsSerializer(serializers.ModelSerializer):
    """
    Serializing all the Actors
    """

    class Meta:
        model = Actor
        fields = ("first_name", "last_name", "date_of_birth", "date_of_death")

