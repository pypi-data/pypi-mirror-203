import pytest

from katalytic import pkg, katalytic


def test_versions():
    modules = {m.__name__: m for m in pkg.get_modules()}
    modules['katalytic'] = katalytic
    for name, module in modules.items():
        assert module.__version__ is not None, (name, module.__version__)
