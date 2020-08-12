# applying augmented Dickey-Fuller unit root test
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller

# setting URLs for Apple, Google and Facebook

url_apple = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&outputsize=full&symbol=AAPL&apikey=F6FR4E0EVKTSNPYQ&datatype=csv"
url_google = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&outputsize=full&symbol=GOOG&apikey=F6FR4E0EVKTSNPYQ&datatype=csv"
url_facebook = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&outputsize=full&symbol=FB&apikey=F6FR4E0EVKTSNPYQ&datatype=csv"

# getting CSV results

a_apple = pd.read_csv(url_apple)
a_google = pd.read_csv(url_google)
a_facebook = pd.read_csv(url_facebook)

# transforming dataframes into numpy arrays with close price (10 years of 365 days - 52 weekends - 8 public holidays)

arr_apple = (a_apple.to_numpy())[0:10*(365-52*2-8),4]
arr_google = (a_google.to_numpy())[0:10*(365-52*2-8),4]
arr_facebook = (a_facebook.to_numpy())[0:10*(365-52*2-8),4]

result_app = adfuller(r_apple)
print('ADF Statistic: %f' % result_app[0])
print('p-value: %f' % result_app[1])
for key, value in result_app[4].items():
    print('\t%s: %.3f' % (key, value))
    
from statsmodels.tsa.stattools import adfuller
result_google = adfuller(r_google)
print('ADF Statistic: %f' % result_google[0])
print('p-value: %f' % result_google[1])
for key, value in result_google[4].items():
    print('\t%s: %.3f' % (key, value))
    
from statsmodels.tsa.stattools import adfuller
result_facebook = adfuller(r_facebook)
print('ADF Statistic: %f' % result_facebook[0])
print('p-value: %f' % result_facebook[1])
for key, value in result_facebook[4].items():
    print('\t%s: %.3f' % (key, value))
