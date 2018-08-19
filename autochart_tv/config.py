from pathlib import Path

import toml
import structlog

from .tools import validate

class InvalidSettingError(Exception): #TODO: used for writing setting from repl
    pass


class Configuration:
    CONFIG_PATH = Path(__file__).parent.parent / 'config.toml'

    CHART_DEFAULT = {'title': 'autochart-tv',
                     'interval': '1m',
                     'timezone': 'UTC',
                     'theme': 'Dark',
                     'barstyle': 'Candles',
                     'studies':['bb']}
    SERVER_DEFAULT = {'debug': True,
                      'port' : 5000}

    CONFIG_DEFAULT = {'chart': CHART_DEFAULT,
                      'server': SERVER_DEFAULT}

    def __init__(self):
        self.logger = structlog.get_logger()
        self.settings = None
        self._load_config_file()

    def get_settings(self):
        self._load_config_file()
        return self.settings

    def get_server_setting(self, setting):
        validate(setting, self.settings['server'], 'server')
        return self.settings['server'][setting]

    def get_chart_setting(self, setting):
        validate(setting, self.settings['chart'], 'chart')
        return self.settings['chart'][setting]

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
