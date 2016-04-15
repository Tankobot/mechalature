class Reader:
    """File-like object for text analysis."""

    def __init__(self, source):
        assert source.read
