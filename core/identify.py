from core import MechalatureError
import shelve

__all__ = [
    'MechalatureEvent',
    'get_info'
]


word_bank = shelve.open('bin/word_bank')


class MechalatureEvent:
    def __init__(self, name: str):
        self.name = name
        self._tags = set()

    def tag(self, terms: set):
        self._tags += terms

    def check(self):
        get_info(self)


class TagError(MechalatureError):
    def __init__(self, msg: str, tags: tuple):
        self.tags = tags

        super().__init__(msg)


possible_tags = (
    'noun',
    'adjective',
    'verb',
    'plural',
    'singular'
)


def get_info(event: MechalatureEvent):
    try:
        tags = word_bank[event.name]
    except KeyError:
        tags = ()
        # TODO
