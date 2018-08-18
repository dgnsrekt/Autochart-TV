# system
from abc import ABC as Abstract
from abc import abstractmethod
import sys

from selenium.common.exceptions import WebDriverException

from autochart_tv.model import AutoChartModel, AutoChartDatabase
from autochart_tv.exchange import ExchangeInterface

from command_prompt import AutoChartPrompt
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
        refresh = False
        for ticker in tickers:
            if ticker:
                print(ticker)
                refresh = AutoChartModel.add(ticker)
        if refresh:
            RefreshCommand().execute()

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


class ACManager:
    def __init__(self, port):
        pass


# sys.exit()

COMMANDS = [ExitCommand(), ClearCommand(), DeleteCommand(), RandomCommand(),
            RandomCryptoCommand(), RandomStockCommand(), ChartCommand(), RefreshCommand()]
COMMANDS = {command.name: command for command in COMMANDS}
COMMANDS['QUIT'] = ExitCommand()

WORD_LIST = [command for command in COMMANDS] + ACSymbols.all_symbols
print(WORD_LIST[:5])

def main():
    ACPrompt = AutoChartPrompt(commands=WORD_LIST)
    ACWebDriver.start()


    while True:
        inp = ACPrompt.get_prompt()
        cmd = inp.split(' ')[0].upper()
        args = inp.split(' ')[1:]
        args = [arg for arg in args if len(arg) > 0]

        try:
            command = COMMANDS[cmd]
            if len(args) > 0:
                command.execute(args)
            else:
                command.execute()
        except KeyError:
            tickers = inp.split(' ')
            tickers = [ticker for ticker in tickers if len(ticker) > 0]
            ChartCommand().execute(*tickers)

        except WebDriverException:
            ExitCommand().execute()

if __name__ == '__main__':
    main()
