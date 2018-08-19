from repl import parse_input


COMMANDS = ['CHART']

def test_parse_input():
    inp = 'CHART TSLA AAPL'
    assert parse_input(inp, commands=COMMANDS) == ('CHART', ['TSLA', 'AAPL'])

def test_parse_input2():
    inp = 'TSLA AAPL BTCUSD'
    assert parse_input(inp, commands=COMMANDS) == (None, ['TSLA', 'AAPL', 'BTCUSD'])

def test_parse_input3():
    inp = ' TSLA AAPL BTCUSD'
    assert parse_input(inp, commands=COMMANDS) == (None, ['TSLA', 'AAPL', 'BTCUSD'])

def test_parse_input4():
    inp = ''
    assert parse_input(inp, commands=COMMANDS) == (None, None)

def test_parse_input_lowercase():
    inp = 'chart tsla aapl'
    assert parse_input(inp, commands=COMMANDS) == ('CHART', ['TSLA', 'AAPL'])
