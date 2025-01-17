**Macro**
1. Get data for markets\
    a. Price data\
    b. Sentiment data\
    c. Options & Futures data
    
2. Market state\
    1 year, 6 month, 3 month, 1 month, 2 weeks, 1 week.    
    a. linear regression, a > 0 or a <0\
    b. Pos/Neg counter, a > 0 or a <0\
    c. Markov state, uuuuu ... ddddd probs, x year counter, vs current state.
    d. Convergence of high and low
3. Repeat market state for each market

**Micro**
1. Get data for markets
2. Market state\
    1 year, 6 month, 3 month, 1 month, 2 weeks, 1 week.    
    a. linear regression, a > 0 or a <0\
    b. Pos/Neg counter, a > 0 or a <0\
    c. Markov state, uuuuu ... ddddd probs, x year counter, vs current state.\
    d. Hidden Markov state
3. Run fundamentals analysis\
    a. Debt decreasing?\
    b. Profit increasing?\
    c. Cashflow increasing?\
    d. General Sentiment analysis?\
    e. News analysis?
4. Run Technical indications\
    a. MA indicator\
    b. MACD indicator\
    c. RSI indicator\
    d. Markov hidden state\
    e. Markov state\
    f. 0-tangent



| Strategy 1 | Strategy 1 | Strategy 1 | Strategy 1 |
| ------------- | ------------- | ------------- | ------------- |
| **Mean reversion** | **Attack Dumps** | **Events** | **Prediction** |
|  | | | |
|  | | | |
| | | | |




the double crossover strategy



LMA = long-term moving average, 60 day sma
SMA = short-term moving average, 15 day sma.

1. Downtrend changes to the uptrend, the price crosses over the short-term, 
and secondly, the short-term crosses over the long-term. This is called the “Golden Cross”.
buy

2. Uptrend changes to the downtrend, firstly, the price crosses under the short-term, 
and secondly, the short-term crosses under the long-term. This is called “Death Cross”.
sell




r^2 = 1 - RSS / TSS

RSS = sum(y-y_predicted)^2
TSS = sum(y-y_mean)^2

from sklearn.metrics import r2_score
score = r2_score(data["Actual Value"], data["Preds"])
print("The accuracy of our model is {}%".format(round(score, 2) *100))

mean absolute error (MAE)

= 1/n sum(1, n) abs(y-y_predicted)

from sklearn.metrics import mean_absolute_error
score = mean_absolute_error(data["Actual Value"], data["Preds"])
print("The Mean Absolute Error of our Model is {}".format(round(score, 2)))

root mean squared error (RMSE)

=sqrt(1/n sum(1,n) (y-y_predicted)^2
      
from sklearn.metrics import mean_squared_error
import numpy as np
score = np.sqrt(mean_absolute_error(data["Actual Value"], data["Preds"]))
print("The Mean Absolute Error of our Model is {}".format(round(score, 2)))

## Min-max strategy?


import math
import pandas as pd
import numpy as np
from scipy.stats import norm, mstats
from datetime import datetime, date, timedelta, timezone
import edge
import edge.edge_mean_reversion as emr
import edge.edge_risk_kit as erk
import TMRW
from statsmodels.stats.outliers_influence import variance_inflation_factor 
import matplotlib.pyplot as plt
from scipy import stats
import yfinance as yf

today = date.today() 
today = datetime(today.year,today.month,today.day) #today
m1 = datetime(today.year,today.month-1,today.day)
m3 = datetime(today.year,today.month-3,today.day)
m6 = datetime(today.year,today.month-5,today.day)
one = datetime(today.year-1,today.month,today.day) #one year ago
three = datetime(today.year-3,today.month,today.day) #one year ago
five = datetime(today.year-5,today.month,today.day) #one year ago

CUR = pd.read_excel(open('E:/Investering/Currencies.xlsx', 'rb'),sheet_name='Currencies')
CUR = list(CUR[CUR['BSYMBOL'].notnull()]['SYMBOL'])
lste = CUR

import pandas as pd
from datetime import datetime, date, timedelta, timezone
import warnings
warnings.filterwarnings("ignore")
from binance.enums import *
import time

import warnings
warnings.filterwarnings("ignore")

run = True

api_key = 'vBrHMZUCDxlfNiAreBj02aUrymSFMGyl1AwJNAP0O7qVlvh07Drq7qQwfQlbYGeS'
api_secret = 'SdzCkiFE5zNjkSvptRVpxQBxlUWZWYrjnRGLp5tzhzJiat79vymOH127zaKHnnCh'

from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
client = Client(api_key, api_secret)
buy = False

while run == True:

    today = date.today() 
    today = datetime(today.year,today.month,today.day+1)
    day7 = datetime(today.year,today.month,today.day) + timedelta(days = -7) 
    today = today.strftime("%d-%m-%Y")
    day7 = day7.strftime("%d-%m-%Y")

    klines = client.get_historical_klines("ADAUSDT", Client.KLINE_INTERVAL_30MINUTE, day7, today)
    data = pd.DataFrame(klines, columns = ['Open time', 'Open','High','Low','Close','Volume','Close time','Quote asset volume','Number of trades','Taker buy base asset volume','Taker buy quote asset volume', 'Ignore'])

    data.Open = data.Open.astype(float)
    data.High = data.High.astype(float)
    data.Low = data.Low.astype(float)
    data.Close = data.Close.astype(float)
    data.Volume = data.Volume.astype(float)
    data = data[['Open','High','Low','Close','Volume']]

    #data = TMRW.DATA.data(Symbol,time,today)
    data['value'] = (data['High'] + data['Low']) / 2
    data.replace([np.inf, -np.inf], 0, inplace=True)
    data = data.fillna(0)

    data['buy_signal'] = False
    data['sell_signal'] = False

    k = 0
    j = 0

    for i in range(len(data)):

        # generate long/buy signal


        if i > 1 and (min(data['value'][j:i])*1.0001 > data['value'][i-1]) and data['value'][i] > data['value'][i-1]:
            data['buy_signal'][i] = True
            k = i-1

        # generate short/sell signal

        if i > 1 and (max(data['value'][k:i])*0.999999 < data['value'][i-1]) and data['value'][i] < data['value'][i-1]:
            data['sell_signal'][i] = True
            j = i


    if data.iloc[-1,6] == True and buy == False:
        buy = True
        order = client.order_market_buy(
        symbol='ADAUSDT',
        quantity=50.5)

    if data.iloc[-1,7] == True and buy == True:
        buy = False
        order = client.order_market_sell(
        symbol='ADAUSDT',
        quantity=50.4)

    time.sleep(25*60)


## Mean reversion?

import math
import pandas as pd
import numpy as np
from scipy.stats import norm, mstats
from datetime import datetime, date, timedelta, timezone
import edge
import edge.edge_mean_reversion as emr
import edge.edge_risk_kit as erk
import TMRW
from statsmodels.stats.outliers_influence import variance_inflation_factor 
import matplotlib.pyplot as plt
from scipy import stats
import yfinance as yf

today = date.today() 
today = datetime(today.year,today.month,today.day) #today
m1 = datetime(today.year,today.month-1,today.day)
m3 = datetime(today.year,today.month-3,today.day)
m6 = datetime(today.year,today.month-5,today.day)
one = datetime(today.year-1,today.month,today.day) #one year ago
three = datetime(today.year-3,today.month,today.day) #one year ago
five = datetime(today.year-5,today.month,today.day) #one year ago

CUR = pd.read_excel(open('E:/Investering/Currencies.xlsx', 'rb'),sheet_name='Currencies')
CUR = list(CUR[CUR['BSYMBOL'].notnull()]['SYMBOL'])
lste = CUR

import pandas as pd
from datetime import datetime, date, timedelta, timezone
import warnings
warnings.filterwarnings("ignore")
from binance.enums import *
import time

run = True

api_key = 'vBrHMZUCDxlfNiAreBj02aUrymSFMGyl1AwJNAP0O7qVlvh07Drq7qQwfQlbYGeS'
api_secret = 'SdzCkiFE5zNjkSvptRVpxQBxlUWZWYrjnRGLp5tzhzJiat79vymOH127zaKHnnCh'

from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
client = Client(api_key, api_secret)
buy = True
p = 0

while run == True and p < 100:

    today = date.today() 
    today = datetime(today.year,today.month,today.day+1)
    day7 = datetime(today.year,today.month,today.day) + timedelta(days = -7) 
    today = today.strftime("%d-%m-%Y")
    day7 = day7.strftime("%d-%m-%Y")

    klines = client.get_historical_klines("TRXUSDT", Client.KLINE_INTERVAL_30MINUTE, day7, today)
    data = pd.DataFrame(klines, columns = ['Open time', 'Open','High','Low','Close','Volume','Close time','Quote asset volume','Number of trades','Taker buy base asset volume','Taker buy quote asset volume', 'Ignore'])
    
    data.Open = data.Open.astype(float)
    data.High = data.High.astype(float)
    data.Low = data.Low.astype(float)
    data.Close = data.Close.astype(float)
    data.Volume = data.Volume.astype(float)
    data = data[['Open','High','Low','Close','Volume']]

    #data = TMRW.DATA.data(Symbol,time,today)
    data['value'] = (data['High'] + data['Low']) / 2
    data.replace([np.inf, -np.inf], 0, inplace=True)
    data = data.fillna(0)

    data['MA5'] = TMRW.FINANCE.twa(data['value'], 10)[9]
    data['MA5'][0] = 0
    data['MA10'] = TMRW.FINANCE.twa(data['value'], 30)[29]
    data['MA10'][0] = 0
    data['MA30'] = TMRW.FINANCE.twa(data['value'], 60)[59]
    data['MA30'][0] = 0
    data['RSI'] = TMRW.FINANCE.RSI(data['value'], 60)
    data['buy_signal'] = False
    data['sell_signal'] = False
    data['short_signal'] = False

    a = list(TMRW.FINANCE.returns(data['value'])['value'])
    a.insert(0,0)
    data['returns'] = a

    pos_neg = []
    for i in range(len(data)):
        if data['returns'][i] >= 0:
            pos_neg.append(1)
        elif data['returns'][i] < 0:
            pos_neg.append(-1)

    data['pos_neg'] = pos_neg
    data['mean_return'] = data['returns'].rolling(window=15).mean().values.flatten()

    for i in range(len(data)):

       # make sure there's no significant trend
        if np.mean(data['pos_neg'][i-20:i]) > 0.01 and data['mean_return'][i] > 0.005:
            next

        elif np.mean(data['pos_neg'][i-20:i]) < -0.01 and data['mean_return'][i] < -0.005:
            next

        else:
            
             # generate long/buy signal
            if i > 10 and (data['MA5'][i] < data['MA30'][i]) and (data['MA30'][i-1] > data['value'][i-1]) and data['RSI'][i] < 1.1*min(data['RSI'][i-5:i]): #  (data['MA5'][i] > data['MA10'][i]) and 
                data['buy_signal'][i] = True

            # generate short/sell signal

            if  i > 10 and (data['MA10'][i] > data['MA30'][i]) and (data['MA30'][i-1] < data['value'][i-1]) and data['RSI'][i] > 0.9*max(data['RSI'][i-5:i]): # (data['MA5'][i] < data['MA10'][i]) and
                data['sell_signal'][i] = True

    

    if data.iloc[-1,10] == True and buy == False:
        buy = True
        order = client.order_market_buy(
        symbol='TRXUSDT',
        quantity=130)

    if data.iloc[-1,11] == True and buy == True:
        buy = False
        order = client.order_market_sell(
        symbol='TRXUSDT',
        quantity=129)
    
    p = p + 1
    time.sleep(25*60)
