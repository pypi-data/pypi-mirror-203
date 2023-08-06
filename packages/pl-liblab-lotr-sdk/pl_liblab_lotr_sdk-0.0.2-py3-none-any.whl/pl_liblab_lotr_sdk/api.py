import requests
from functools import cache

from .models import Movie, Quote


class Client:
    BASE_URL = 'https://the-one-api.dev/v2'

    def __init__(self, api_key):
        self.headers = {"Authorization": f"Bearer {api_key}"}

    @cache
    def get_movie(self, movie_id=None):
        """
        Get all movies if no movie_id passed in.
        """
        uri = "/movie"
        if movie_id:
            uri += f"/{movie_id}"
        res = self._send_request(uri)
        return [Movie(x, self) for x in res]

    @cache
    def get_quote(self, movie_id):
        """
        Get all quotes for a specific movie.
        TODO: Extend to include fetching individual quotes by id
              and to fetch all quotes
        """
        path = f'/movie/{movie_id}/quote'
        res = self._send_request(path)
        return [Quote(quote, self) for quote in res]

    def get_book(self, book_id):
        pass

    def get_character(self, character_id):
        pass

    def get_chapter(self, chapter_id):
        pass

    def _send_request(self, path):
        uri = f"{Client.BASE_URL}{path}"
        res = requests.get(uri, headers=self.headers)
        res.raise_for_status()
        data = res.json()

        # TODO: Handle pagination. Either provide an interface to lazily get
        # more items (hard) or just fetch all pages worth of data (easy).
        if data.get('total') > data.get('limit'):
            raise Exception("API Data exceeds limit")

        return data.get('docs', [])
