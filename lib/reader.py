"""Return bite size pieces of text documents."""

import string


class CharacterError(Exception):
    pass


class ResearchError(Exception):
    pass


class Reader:
    """Read your text file in pieces."""

    def __init__(self, target):
        """Declare Reader instance variables.

        Attributes:
            target (file): The file to pull events from.
        """

        self.target = target
        self.checkFirst = ''

    def pull(self):
        """Pull a single text event from the target.

        Return:
            event (tuple): Next event from target.
        """

        target = self.target

        # Track loop
        time_loop = 0
        # Create event
        data = ''
        data_type = None
        while True:
            if len(self.checkFirst):
                char = self.checkFirst
                self.checkFirst = ''
            else:
                char = target.read(1)

            if char in string.ascii_letters:
                data += char
                data_type = 'word'
            elif char in string.whitespace:
                break
            elif (char in string.punctuation) and (time_loop != 0):
                self.checkFirst = char
                break
            elif (char in string.punctuation) and (time_loop == 0):
                data = char
                data_type = 'punctuation'
                break
            else:
                raise CharacterError(char)
            time_loop += 1
        return data_type, data

    def pull_multiple(self, amount):
        """Pull multiple text events from the target.

        Parameters:
            amount (int): Specify number of events to pull.

        Return:
            events (list): Multiple events from target.
        """

        events = []

        for i in range(amount):
            events.append(self.pull())

        return events


# Perform Word Database Caching
# TODO


# Perform Word Database Search
def research(word):
    if type(word) != 'str':
        raise ResearchError('Word not str')

    pass
