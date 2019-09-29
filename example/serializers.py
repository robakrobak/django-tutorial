from rest_framework import serializers

from example.models import Movie, Genre


class GenreSerializer(serializers.ModelSerializer):
    """
    Serializing all the Genre
    """

    class Meta:
        model = Genre
        fields = ("id", "name")
        # po tym tworzymy widok Genre -gatunku


class MovieSerializer(serializers.ModelSerializer):
    """
    Serializing all the Movies
    """

    # genre = GenreSerializer()   #wyświetla zmaiast id = 3 to nazwę genre czyli np horror i id = 3

    class Meta:
        model = Movie
        fields = ("id", "name", "year", "released", "genre", "viewed")


class MovieMiniSerializer(serializers.ModelSerializer):
    """
    Serializing all the Movies
    """

    class Meta:
        model = Movie
        fields = ("id", "name")
