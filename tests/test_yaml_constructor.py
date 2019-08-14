import pytest

from type_registry import load_yaml_str, register


@register('yaml-simple', x=10)
class Simple:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def test_load_yaml_str_raises_exception_if_type_is_not_found():
    test_config = '''
base:
    __factory__: no-one
    '''

    with pytest.raises(ValueError):
        load_yaml_str(test_config)


def test_load_yaml_str_returns_constructed_type():
    test_config = '''
base:
    __factory__: yaml-simple
    y: 20
    '''

    actual = load_yaml_str(test_config)
    assert 'base' in actual
    assert type(actual['base']) is Simple


def test_load_yaml_str_constructs_with_correct_values():
    test_config = '''
base:
    __factory__: yaml-simple
    y: 20
    '''

    actual = load_yaml_str(test_config)
    base = actual['base']
    assert base.x == 10
    assert base.y == 20
