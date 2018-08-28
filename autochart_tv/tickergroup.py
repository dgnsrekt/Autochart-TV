from datetime import datetime
from collections import OrderedDict
from functools import reduce


class TickerGroup:
    def __init__(self, name, time, major_tickers=[], minor_tickers=[]):

        assert isinstance(time, datetime)
        self.name = name
        self.time = time
        self.majors = major_tickers
        self.minors = minor_tickers

        self.all_tickers = self.majors + self.minors

    def __lt__(self, other):
        return self.time > other.time

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __add__(self, other):
        TickerGroupObjects = sorted([self, other])
        name = reduce(lambda x, y: x.name + ', ' + y.name, TickerGroupObjects)
        time = TickerGroupObjects[0].time
        majors = []
        minors = []

        for tgo in TickerGroupObjects:
            majors += tgo.majors
            minors += tgo.minors

        # removes duplicates while retaining order
        majors = list(OrderedDict.fromkeys(majors))
        minors = list(OrderedDict.fromkeys(minors))

        return TickerGroup(name, time, majors, minors)

    def __repr__(self):
        return self.name

    def __getitem__(self, index):
        return self.all_tickers[index]

    def __str__(self):
        str__ = f'class: {self.__class__.__name__}\n'
        for attr in vars(self).items():
            try:
                str__ += f'{attr[0]}: {attr[1]} {len(attr[1])}\n'
            except TypeError:
                str__ += f'{attr[0]}: {attr[1]}\n'
        else:
            return str__
