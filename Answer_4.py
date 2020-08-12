
PNL_apple = np.multiply(f_apple, r_apple)
PNL_google = np.multiply(f_google, r_google)
PNL_facebook = np.multiply(f_facebook, r_facebook)

sharpe_apple = PNL_apple.mean()/PNL_apple.std()
sharpe_google = PNL_google.mean()/PNL_google.std()
sharpe_facebook = PNL_facebook.mean()/PNL_facebook.std()

print(sharpe_apple)
print(sharpe_google)
print(sharpe_facebook)
