from statsmodels.tsa.stattools import adfuller
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
