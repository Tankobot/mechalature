from core import MechalatureError
from core import identify
import io
import sys
import string

__all__ = [
    'Reader',
    'ReaderValueError',
    'ReaderError'
]


class ReaderError(MechalatureError):
    def __init__(self, msg: str):
        super().__init__(msg)


class ReaderValueError(ReaderError):
    def __init__(self, msg: str, val: int):
        self.val = val

        super().__init__(msg)


class Reader:
    read_size = 2 ** 10
    carry_size = 2 ** 6

    def __init__(self, source: io.TextIOBase = sys.stdout):
        """File-like object for text analysis."""

        self.source = source
        self._buffer = ''
        self._new_buffer = ''
        self._event_temp = []

    def read(self, n=0):
        """Retrieve events from the source.

        The read method only reads the source and passes it to the necessary hidden methods to process the text
        further and convert it into the usable events. `n` defaults to `0` which will have the method read the source
        until the entire source is finished.

        :param n: Specify number of events to grab

        :return: A list of events describing the document
        :rtype: list

        """

        # store a list of all new events until they can be returned
        pulled = []

        while (len(pulled) < n) or (not n):
            # read a chunk of the file to be parsed
            self._buffer += self.source.read(self.read_size)

            # make sure that characters are allowed and characters have been read
            try:
                self._check_chars(self._buffer)
            except EOFError:
                break

            # check if an event has already been parsed or if new ones have to be looked up
            if self._event_temp:
                pulled += self._event_temp.pop(0)
            else:
                self._event_temp += self._parse()

        return pulled

    def _parse(self):
        """Separate buffer into events."""

        # separation of words and events
        pieces = self._buffer.split(' ')
        words = map(self._tag, pieces)
        words = [word for word in words if word]

        self.clean_buffer()

        return words

    @staticmethod
    def _tag(word: str):
        """Convert words to events.

        :param word: Word to create event from

        :return: Event based on word
        :rtype: identify.MechalatureEvent

        """

        word = word.lower()

        event = identify.MechalatureEvent(word)
        event.tag({'word'})

        return event

    _supported_characters = \
        string.ascii_letters + \
        string.punctuation + \
        string.whitespace

    @classmethod
    def _check_chars(cls, chars: str):
        """Check that new characters are valid.

        :param chars: Characters to check

        """

        # check for end of file
        if not chars:
            raise EOFError('read eof')

        # check for characters that aren't recognizable
        for bad_char in chars:
            if bad_char in cls._supported_characters:
                raise ReaderValueError('unsupported character found: %s' % bad_char,
                                       cls._supported_characters)

    def clean_buffer(self):
        # TODO

        if len(self._buffer) > self.carry_size:
            raise ReaderValueError('buffer limit reached: %s > %s' % (len(self._buffer), self.carry_size),
                                   len(self._buffer))
