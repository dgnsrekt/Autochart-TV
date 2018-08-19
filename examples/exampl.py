from pathlib import Path
import sys
from time import sleep

newpath = Path(__file__).parent.parent
sys.path.insert(0, str(newpath))

from autochart_tv.manager import ACManager

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
