# Evx regpredict mlbot

This is a simplified version of [evxpredictor](https://pypi.org/project/evxpredictor/) package used to generate buy and sell signals for crypto and conventional stock markets based on the excess volume indicator(EVX). EVX is a concept where the bid-ask spread is estimated inherently from current market prices. 

You can read more about Evx in the whitepaper [here](https://www.researchgate.net/publication/345313655_DeFiPaper)  
# Installation
Install regpredict with `python3 -m pip install regpredict`  
# Usage

In your python script simply import the module and use as follows:

```  
from regpredict.regbot import signal
print(signal(20,65))
```
The above methods take an assets opening and closing prices of the asset based on the time interval you have chosen. A zero classification output would instruct the user to sell, while one output means don't sell or buy if the asset is not already present in the orders.  

# Testing an entire dataframe
Testing of a dataframe for correct buy, sell signals is as simple as applying the function as follows:  

```
import pandas as pd
from regpredict.regbot import signal

df = pd.read_csv('../../../path/to_your.csv')

y_pred = []
def getSignal(open,close):
    return signal(open,close)


df = df[df['buy'] == 1]
print(df.head())

df['signal'] = df.apply(lambda row: getSignal(row['open'], row['close']), axis=1)

print(df.head())

print(len(df[df['signal'] == df['buy']]), len(df))

```

Your original data must already have some presumed 'buy' signal.

# Warning
This is not financial advise. Regpredict is entirely on its preliminary stages. Use it at your own risk.