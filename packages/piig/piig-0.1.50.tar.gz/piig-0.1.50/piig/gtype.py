import typing

import piig


class CompiledCode:
    _gen: typing.Generator
    _with_version: bool

    def __init__(self, gen, *, with_version):
        self._gen = gen
        self._with_version = with_version

    def __call__(self):
        yield from self._gen
        if self._with_version:
            yield f"( {piig.__version__} )\n"
