"""Start mechalature automatic annotation.

Options: (not implemented)
    -x          | Run in experimental mode.
    -d          | Disable network connection.
    -c          | Disable text data contribution.
    -h, --help  | Display this docstring.
"""

# import argparse
#
# parser = argparse.ArgumentParser(description='Start mechalature automatic annotation.')

mode = input('Mode n/x: ')


class Error(Exception):
    def __init__(self, message):
        print(message)

if mode == 'n':
    tool_set = 'normal'
elif mode == 'x':
    tool_set = 'experimental'
else:
    raise Error('Unrecognized mode')
