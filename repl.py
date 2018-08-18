from manager import ACManager
from command_prompt import AutoChartPrompt

def main():
    ACM = ACManager()
    WORD_LIST = [command for command in ACM.commands] + ACM.tickers
    ACPrompt = AutoChartPrompt(commands=WORD_LIST)

    with ACM as acm:
        while True:
            inp = ACPrompt.get_prompt()
            cmd = inp.split(' ')[0].upper()
            args = inp.split(' ')[1:]
            args = [arg for arg in args if len(arg) > 0]

            try:
                command = acm[cmd]
                if len(args) > 0:
                    command.execute(args)
                else:
                    command.execute()
            except KeyError:
                tickers = inp.split(' ')
                tickers = [ticker for ticker in tickers if len(ticker) > 0]
                acm['CHART'].execute(*tickers)

            except WebDriverException:
                acm['EXIT'].execute(*tickers)

if __name__ == '__main__':
    main()
