from rest_framework import serializers

from example.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    """
    Serializing all the Movies
    """

    class Meta:
        model = Movie
        fields = ("id", "name", "year", "released", "genre")
