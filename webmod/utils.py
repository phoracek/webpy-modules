#!/usr/bin/env python
"""
General Utilities
(part of web.py modules)
"""

__all__ = [
    "Storage", "storage"
]


class Storage(dict):
    """
    A Storage object is like a dictionary except `obj.foo` can be used
    in addition to `obj['foo']`. (part of web.py)

        >>> o = storage(a=1)
        >>> o.a
        1
        >>> o['a']
        1
        >>> o.a = 2
        >>> o['a']
        2
        >>> del o.a
        >>> o.a
        Traceback (most recent call last):
            ...
        AttributeError: 'a'

    """
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError, e:
            raise AttributeError, e

    def __setattr__(self, key, value):
        self[key] = value

    def __delattr__(self, key):
        try:
            del self[key]
        except KeyError, e:
            raise AttributeError, e

    def __repr__(self):
        return '<Storage ' + dict.__repr__(self) + '>'

storage = Storage


if __name__ == "__main__":
    import doctest
    doctest.testmod()
