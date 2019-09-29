from rest_framework import serializers

from example.models import Movie, Genre


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
        fields = ("id", "name", "year", "released", "genre", "viewed", "is_delete")


class MovieMiniSerializer(serializers.ModelSerializer):
    """
    Serializing all the Movies
    """

    class Meta:
        model = Movie
        fields = ("id", "name")