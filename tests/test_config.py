import toml
import pytest
from pathlib import Path

from autochart_tv.config import Configuration
from autochart_tv.tools import ValidationError


def test_import():
    pass


@pytest.fixture
def configuration(monkeypatch, tmpdir):
    CONFIG_TEST_PATH = Path(tmpdir.mkdir('temp').join('config.toml'))
    monkeypatch.setattr(Configuration, 'CONFIG_PATH', CONFIG_TEST_PATH)
    return Configuration()


def test_config_file_not_found_error(configuration):
    configuration.CONFIG_PATH.unlink()  # deletes configfile
    assert not configuration.CONFIG_PATH.exists()
    with pytest.raises(FileNotFoundError):
        configuration._read_config_file()

    configuration._load_config_file()  # creates new configfile
    assert configuration.CONFIG_PATH.exists()


def test_configuration_get_server_setting(configuration):
    assert configuration.get_server_setting('title') == 'autochart-tv'


def test_configuration_get_server_setting_validation_error(configuration):
    with pytest.raises(ValidationError):
        configuration.get_server_setting('bad-title')


def test_create_default_config_file(configuration):
    test_toml = toml.dumps({'server': {'title': 'faketitle'}})
    with open(configuration.CONFIG_PATH, 'w') as file:
        file.write(test_toml)
    configuration._load_config_file()

    assert not configuration.get_server_setting('title') == 'autochart-tv'

    configuration._create_default_config_file()
    assert configuration.get_server_setting('title') == 'autochart-tv'
