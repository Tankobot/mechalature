class Reader:
    """File-like object for text analysis."""

    def __init__(self, source):
        self.source = source
        self.last = None
        self.char = ''

    def read(self, n=1):
        pulled = 0
        while pulled < n:
            self.char = self.char or self.source.read(1)

            # TODO 

            self.char = ''
