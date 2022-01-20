import pyupbit
import pandas as pd

chart = pd.DataFrame(pyupbit.get_ohlcv("KRW-BTC",interval="minute60",count=24,to="20211229 09:10:00"))

chart.insert(len(chart.columns),'fluctuation',0)
chart.insert(len(chart.columns),'percentage',0)
for open,close,fluc in zip(chart['open'],chart['close'],range(24)) : 
    chart['fluctuation'][fluc] = close-open
    chart['percentage'][fluc] = (close-open)/open*100
print(chart)
