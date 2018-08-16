from .options import BARSTYLES, INTERVALS, TIMEZONES, THEMES, STUDIES
from .tools import validate


class Chart:

    def __init__(self,
                 symbol='BITFINEX:BTCUSD',
                 interval='1d',
                 timezone='UTC',
                 theme='Dark',
                 barstyle='Candles',
                 studies=['bb'],
                 settings=None):

        if settings:
                interval =  settings['chart']['interval']
                timezone =  settings['chart']['timezone']
                theme =  settings['chart']['theme']
                barstyle =  settings['chart']['barstyle']
                studies =  settings['chart']['studies']

        validate(interval, INTERVALS, 'Interval')
        validate(timezone, TIMEZONES, 'Timezone')
        validate(theme, THEMES, 'Theme')
        validate(barstyle, BARSTYLES, 'Barstyle')

        self.studies = list()
        for study in studies:
            validate(study, STUDIES, 'Study')
            self.studies.append(STUDIES[study])

        self.symbol = symbol
        self.interval = INTERVALS[interval]
        self.timezone = TIMEZONES[timezone]
        self.theme = theme
        self.barstyle = BARSTYLES[barstyle]

    def __repr__(self):
        repr_ = f'Symbol: {self.symbol}\n'
        repr_ += f'Interval: {self.interval}\n'
        repr_ += f'Timezone: {self.timezone}\n'
        repr_ += f'Theme: {self.theme}\n'
        repr_ += f'Barstyle: {self.barstyle}\n'
        return repr_
