import pandas as pd
import matplotlib.pyplot as plt

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

N_apple = arr_apple.size
N_google = arr_google.size
N_facebook = arr_facebook.size

PNL_apple = np.multiply(f_apple, r_apple)
PNL_google = np.multiply(f_google, r_google)
PNL_facebook = np.multiply(f_facebook, r_facebook)

sharpe_apple = PNL_apple.mean()/PNL_apple.std()
sharpe_google = PNL_google.mean()/PNL_google.std()
sharpe_facebook = PNL_facebook.mean()/PNL_facebook.std()

print(sharpe_apple)
print(sharpe_google)
print(sharpe_facebook)
