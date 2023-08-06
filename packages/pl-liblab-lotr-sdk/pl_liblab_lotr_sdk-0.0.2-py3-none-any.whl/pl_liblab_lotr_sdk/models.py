import inflection


class Entity:
    def __init__(self, payload, api):
        self._api = api
        self._raw = payload

        # Take the payload, camel case the key and add it as an attribute.
        for key, value in payload.items():
            camel_key = inflection.underscore(key)
            setattr(self, camel_key, value)


class Movie(Entity):
    def __init__(self, *args, **kwargs):
        super(Movie, self).__init__(*args, **kwargs)

    def quotes(self):
        return self._api.get_quote(self._id)


class Quote(Entity):
    def __init__(self, *args, **kwargs):
        super(Quote, self).__init__(*args, **kwargs)

    def movie(self):
        return self._api.get_movie(movie_id=self.movie)


class Character(Entity):
    pass


class Book(Entity):
    pass


class Chapter(Entity):
    pass
