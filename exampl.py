from repl import ACManager
from time import sleep

with ACManager() as ACM:
    sleep(2)
    ACM['CHART'].execute('AAPL')
    sleep(2)
    ACM['CHART'].execute('BTCUSDT', 'TSLA')
    sleep(2)
    ACM['RANDOM'].execute()
    sleep(2)
    ACM['RANDOMCRYPTO'].execute(9)
    sleep(5)
