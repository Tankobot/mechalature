from typing import Union
import string


class LiteraryParser:
    def __init__(self, source):
        """File-like object for parsing literature.

        :param source: File-like object for pulling raw text from
        :ivar self.stack: list of recently read characters

        """

        assert source.read, 'source is missing read attribute: %r' % source

        self.source = source
        self.stack = []

    def read(self, n=1) -> Union[Event, list]:
        pulled = []
        while len(pulled) < n:
            self.stack.append(self.source.read(1))
            result = self.check_stack()
            pulled.append(result)

            if result is ParserEOF:
                return pulled
        return tuple(pulled)

    def check_stack(self) -> bool:
        pass


class Event:
    pass


class ParserEOF(Event):
    pass
