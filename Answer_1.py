import pandas as pd
import matplotlib.pyplot as plt

url_apple = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&outputsize=full&symbol=AAPL&apikey=F6FR4E0EVKTSNPYQ&datatype=csv"
url_google = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&outputsize=full&symbol=GOOG&apikey=F6FR4E0EVKTSNPYQ&datatype=csv"
url_facebook = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&outputsize=full&symbol=FB&apikey=F6FR4E0EVKTSNPYQ&datatype=csv"

a_apple = pd.read_csv(url_apple)
a_google = pd.read_csv(url_google)
a_facebook = pd.read_csv(url_facebook)

arr_apple = (a_apple.to_numpy())[0:10*(365-52*2-8),4]
arr_google = (a_google.to_numpy())[0:10*(365-52*2-8),4]
arr_facebook = (a_facebook.to_numpy())[0:10*(365-52*2-8),4]
