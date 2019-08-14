import pytest

from type_registry import register, register_library, find_type


@register('simple', x=10)
class SimpleType:
    def __init__(self, x):
        self.x = x


def test_register_creates_correct_type():
    x = find_type('simple')

    assert x is not None
    assert x['factory_method'] is SimpleType


def test_register_raises_exception_for_nonexistent_type():
    with pytest.raises(ValueError):
        x = find_type('not-me')


def test_register_supplies_correct_default_values():
    x = find_type('simple')

    assert x is not None
    assert x['default_values']['x'] == 10
