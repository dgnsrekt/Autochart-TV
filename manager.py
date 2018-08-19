# system
from abc import ABC as Abstract
from abc import abstractmethod
import sys

from selenium.common.exceptions import WebDriverException

from autochart_tv.model import AutoChartModel, AutoChartDatabase
from autochart_tv.exchange import ExchangeInterface

from autochart_tv.webdriver import AutoChartWebDriver

ACWebDriver = AutoChartWebDriver() # some settings init here
ACSymbols = ExchangeInterface()

class Command(Abstract):
    @property
    def name(self):
        return str(self).split('Command')[0].upper()

    @abstractmethod
    def execute(self):
        pass

    def __repr__(self):
        return self.__class__.__name__

class RefreshCommand(Command):
    def execute(self, *args):
        try:
            ACWebDriver.refresh()
        except WebDriverException:
            ACWebDriver.quit()
            sys.exit()

class ExitCommand(Command):
    def execute(self, *args):
        print('exiting...')
        ACWebDriver.quit()
        sys.exit()

class ClearCommand(Command):
    def execute(self, *args):
        AutoChartModel.clear_all()
        RefreshCommand().execute()
        print('clearing all')

class DeleteCommand(Command):
    def execute(self, *args):
        AutoChartModel.delete_last()
        RefreshCommand().execute()


class ChartCommand(Command):
    def execute(self, *tickers):
        refresh = []
        for ticker in tickers:
            if ticker:
                # print(ticker)
                is_data_new = AutoChartModel.add(ticker)
                refresh.append(is_data_new)
        if True in refresh:
            RefreshCommand().execute() #TODO: Alert sound here

class RandomCommand(Command):
    def execute(self, *args):
        print(args)
        try:
            args = int(args[0][0])
            print(f'randoming {args}')
        except (ValueError, IndexError, TypeError) as e:
            args = 1
            print('random one')
        finally:
            tickers = ACSymbols.get_random_symbols(args)
            print(tickers)
            ChartCommand().execute(*tickers)

class RandomCryptoCommand(Command):
    def execute(self, *args):
        try:
            args = int(args[0][0])
            print(f'randoming {args}')
        except (ValueError, IndexError, TypeError) as e:
            args = 1
            print('random one')
        finally:
            tickers = ACSymbols.get_random_crypto(args)
            print(tickers)
            ChartCommand().execute(*tickers)


class RandomStockCommand(Command):
    def execute(self, *args):
        try:
            args = int(args[0][0])
            print(f'randoming {args}')
        except (ValueError, IndexError, TypeError) as e:
            args = 1
            print('random one')
        finally:
            tickers = ACSymbols.get_random_stock(args)
            print(tickers)
            ChartCommand().execute(*tickers)

class ScreenShotCommand(Command):
    def execute(self, *args):
        ACWebDriver.screenshot()

class ACManager:
    _COMMANDS = [ExitCommand(), ClearCommand(), DeleteCommand(), RandomCommand(),
                RandomCryptoCommand(), RandomStockCommand(), ChartCommand(), RefreshCommand(),
                ScreenShotCommand()]

    def __init__(self):
        self.commands = dict()
        self._initialize_commands()
        self.tickers = ACSymbols.all_symbols

    def _initialize_commands(self):
        self.commands = {command.name: command for command in self._COMMANDS}
        self.commands['QUIT'] = ExitCommand()

    def __enter__(self):
        ACWebDriver.start()
        return self.commands

    def __exit__(self, *args, **kwargs):
        print('exiting')
        ACWebDriver.quit()
