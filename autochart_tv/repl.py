from autochart_tv.manager import ACManager
from autochart_tv.prompt import AutoChartPrompt

from selenium.common.exceptions import WebDriverException

#TODO: ADD DEBUG FLAG

def parse_args(input_):
    parsed = [inp.upper() for inp in input_ if len(inp) > 0]
    if parsed:
        return parsed
    return None

def parse_input(input_, commands=[]):
    split = input_.split(' ')
    clean = [s.upper() for s in split if len(s) > 0]

    if len(clean) < 1:
        return (None, None)
    elif clean[0] in commands:
        cmd = clean[0]
        args = parse_args(clean[1:])
    else:
        cmd = None
        args = parse_args(clean)
    return (cmd, args)

def start_ac_repl():
    ACM = ACManager()
    WORD_LIST = [command for command in ACM.commands] + ACM.tickers
    ACPrompt = AutoChartPrompt(commands=WORD_LIST)

    with ACM as acm:
        while True:
            inp = ACPrompt.get_prompt()
            cmd, args = parse_input(inp, commands=ACM.commands)

            try:
                command = acm[cmd]
                if args:
                    command.execute(args)
                else:
                    command.execute()

            except KeyError:
                if args:
                    acm['CHART'].execute(*args)

            except WebDriverException:
                acm['EXIT'].execute(*tickers)

if __name__ == '__main__':
    start_ac_repl()
