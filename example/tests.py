from django.test import TestCase

# Create your tests here.

from django.test import TestCase
from example.models import Movie, Genre
from example.forms import MovieForm, GenreForm


class SimpleTestCase(TestCase):
    def setUp(self):
        self.genre = Genre.objects.create(name="Horror")
        self.movie = Movie.objects.create(
            name='Dracula',
            year=1989,
            released='02-11-1987',
            genre=self.genre,
        )

    def tearDown(self):
        self.movie.delete()
        self.genre.delete()

    def test_max_lenght(self):
        form = MovieForm(data={'name': 'X' * 200})
        self.assertFalse(form.is_valid())

    def test_initial(self):
        form = MovieForm(instance=self.movie)
        self.assertEqual(form.initial['name'], self.movie.name)

    def test_int_test(self):
        form = MovieForm(data={'year': 'X' * 200})
        self.assertFalse(form.is_valid())

    def test_valid_form(self):
        form = MovieForm(data={
            'name': 'This was not it',
            'year': 1234,
            'released': '03-03-1111',
            'genre': self.genre.id}
        )
        self.assertTrue(form.is_valid())

    def test_genre_edit(self):
        form = GenreForm(data={
            'name': 'Komedia'
        })
        self.assertTrue(form.is_valid())

