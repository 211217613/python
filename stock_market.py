#! /usr/bin/python3
# ref: https://cdn.ampproject.org/c/s/ntguardian.wordpress.com/2016/09/19/introduction-stock-market-data-python-1/amp/

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader as  web # For importing data
import datetime
# For jupyter notebooks
# %matplotlib inline

# set time frame for pulling data
start = datetime.datetime(2016,1,1)
end = datetime.date.today()

# Pull apple stock data
apple = web.DataReader("AAPL", "yahoo", start, end)
google = web.DataReader("GOOG", "yahoo", start, end)
microsoft = web.DataReader("MSFT", "yahoo", start, end)
stocks = pd.DataFrame({"AAPL": apple['Adj Close'],
                        "GOOG": google['Adj Close'],
                        "MSFT": microsoft['Adj Close']
                        })

#apple['Adj Close'].plot(grid=True)
stocks.plot(secondary_y = ['AAPL', 'MSFT'], grid=True)

#print(apple.head())
#print(stocks.head())

# df.apply(arg) will apply the function arg to each column in df, and return a DataFrame with the result
# Recall that lambda x is an anonymous function accepting parameter x; in this case, x will be a pandas Series object

stock_return = stocks.apply(lambda x: x / x[0])
stock_return.head()
stock_return.plot(grid=True).axhline(y = 1, color = 'black', lw = 2)
# Take log difference 
stock_change = stocks.apply(lambda x: np.log(x) - np.log(x.shift(1)))
print(stock_change.head())
plt.show()
