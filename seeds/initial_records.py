from contentagregator.modules.redactor_zone.models import Article_categories

from flask_seeder import Seeder, Faker, generator
from flask_seeder.generator import Generator

# Custom generators

class CustomFromListGenerator(Generator):
    """takes a list with elements that will be added to database one by one"""

    def __init__(self, lines: [], start=0, end=99, **kwargs):
        super().__init__(**kwargs)
        self._lines = lines
        self._start = start
        self.end = end
        self._next = self.start

    @property
    def start(self):
        return self._start

    @start.setter
    def start(self, value):
        self._start = value
        if self._next < self._start:
            self._next = self._start

    def generate(self):
        value = self._lines[self._next]
        self._next += 1

        return value


class ArticleCategories(Seeder):
    def __init__(self):
        super().__init__()
        self.priority = 4

    def run(self):
        faker = Faker(
            cls=Article_categories,
            init={
                "category_id" : generator.Sequence(),
                "category_name" : CustomFromListGenerator(["games", "music", "travel", "sport", "documentary","captured", "technology", "fashion", "movies"]),
            }
        )

        for record in faker.create(9):
            print("Adding:", record)
            self.db.session.add(record)
        self.db.session.commit()




