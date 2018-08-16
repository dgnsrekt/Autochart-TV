from autochart_tv.tools import ValidationError, validate

import pytest


def test_import():
    pass


@pytest.fixture
def list_validator():
    return ['a', 'b', 'c']


def test_validate_list(list_validator):
    validate('a', list_validator, 'list_validator')


def test_validate_list_throws_error(list_validator):
    with pytest.raises(ValidationError):
        validate('d', list_validator, 'list_validator')


def test_validate_set(list_validator):
    validate('a', set(list_validator), 'set')


def test_validate_set(list_validator):
    with pytest.raises(ValidationError):
        validate('d', set(list_validator), 'set')


@pytest.fixture
def dict_validator():
    return {'a': 1, 'b': 2, 'c': 3}


def test_validate_dict(dict_validator):
    validate('a', dict_validator, 'dict_validator')


def test_validate_dict_throws_error(dict_validator):
    with pytest.raises(ValidationError):
        validate('d', dict_validator, 'dict_validator')
