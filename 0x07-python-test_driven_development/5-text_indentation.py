#!/usr/bin/python3
"""text_indentation(text)

One method that takes one argument: text
"""


def text_indentation(text):
    """
    Prints text with newlines after . or ? or :
    Leading/trailing spaces will be stripped.
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    text = text.replace('. ', '.') \
               .replace('.', '.\n\n') \
               .replace('? ', '?') \
               .replace('?', '?\n\n') \
               .replace(': ', ':') \
               .replace(':', ':\n\n')
    lines = text.splitlines(keepends=True)
    newtext = ''
    for i in lines:
        newtext += i.strip(' ')
    print(newtext, end='')
