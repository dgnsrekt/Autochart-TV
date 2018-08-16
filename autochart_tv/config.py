from pathlib import Path

import toml
import structlog

from .tools import validate


class Configuration:
    CONFIG_PATH = Path(__file__).parent.parent / 'config.toml'

    SERVER_DEFAULT = {'title': 'autochart-tv'}

    CONFIG_DEFAULT = {'server': SERVER_DEFAULT}

    def __init__(self):
        self.logger = structlog.get_logger()
        self.settings = None
        self._load_config_file()

    def get_server_setting(self, setting):
        validate(setting, self.settings['server'], 'server')
        return self.settings['server'][setting]

    def _read_config_file(self):
        with open(Configuration.CONFIG_PATH, 'r') as file:
            return toml.loads(file.read())

    def _load_config_file(self):
        try:
            self.settings = self._read_config_file()
        except FileNotFoundError:
            self._create_default_config_file()
            self.settings = self._read_config_file()

    def _create_default_config_file(self):
        with open(Configuration.CONFIG_PATH, 'w') as file:
            default_toml = toml.dumps(Configuration.CONFIG_DEFAULT)
            file.write(default_toml)
            self.logger.info('Config file created with default settings.')
            self.logger.info(f'{Configuration.CONFIG_PATH}')
        self._load_config_file()

    def __repr__(self):
        return str(self.settings)
