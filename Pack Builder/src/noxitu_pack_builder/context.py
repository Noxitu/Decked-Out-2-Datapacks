from typing import Any


_CONTEXT = None


class Context:
    def __enter__(self):
        global _CONTEXT
        _CONTEXT = {}

    def __exit__(self, *_):
        global _CONTEXT
        _CONTEXT = None


class ContextStorage:
    def __init__(self, key, init):
        self._key = key
        self._init = init

    def _value(self):
        if self._key not in _CONTEXT:
            _CONTEXT[self._key] = self._init()

        return _CONTEXT[self._key]

    def __getattr__(self, name):
        return getattr(self._value(), name)

    def __iter__(self):
        return iter(self._value())
    
    def __getitem__(self, name):
        return self._value()[name]
    
    def __setitem__(self, name, value):
        self._value()[name] = value


context = Context()
