# Source: https://www.quantifiedstrategies.com/pairs-trading-strategy-python/

import statsmodels.api as sm
import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller


# data start and end dates
start = "2015-01-01"
end = "2023-01-01"

# Stock pairs to try
name_stock1 = "BAC" # Bank of America
name_stock2 = "JPM" # JP Morgan
#
# name_stock1 = "AMD" # AMD
# name_stock2 = "NVDA" # Nvidia
# name_stock2 = "INTC" # Intel
#
# name_stock1 = "PEP" # Pepsi
# name_stock2 = "KO" # Coca Cola
#
# name_stock1 = "FMC1.HM" # Ford
# name_stock2 = "8GM.HM" # General Motors


# download data
stock1 = yf.Ticker(name_stock1)
stock1_data = stock1.history(interval="1d", start=start, end=end)

stock2 = yf.Ticker(name_stock2)
stock2_data = stock2.history(interval="1d", start=start, end=end)


# Chart the prices, normalized by the first closing price
stock1_close_relative = stock1_data["Close"]/stock1_data["Close"][0] * 100
stock2_close_relative = stock2_data["Close"]/stock2_data["Close"][0] * 100

plt.plot(stock1_close_relative, label= name_stock1)
plt.plot(stock2_close_relative, label= name_stock2)
plt.xlabel("Time")
plt.ylabel("Relative Close Price")
plt.legend()
plt.show()


# Set up a regression model
# (the error terms of the lin regression will be used to generate entry & exit signals)
Y = np.log(stock2_data["Close"])
X = np.log(stock1_data["Close"])
X = sm.add_constant(X)  # for why this is necessary, see https://tedboy.github.io/statsmodels_doc/generated/generated/statsmodels.api.OLS.html#statsmodels.api.OLS
model = sm.OLS(Y,X)
results = model.fit() 
results.params


# Get spread of (log'ed) prices (the error terms)
# (spread here: difference between the closing prices of the two stocks)
alpha = results.params.values[0] # constant term
beta = results.params.values[1] # slope term
errors = Y - (alpha + X["Close"]*beta) # rearranged lin regression formula to get the errors

#plot the errors
# errors.plot(label = f"x={name_stock1}; y={name_stock2} \n {name_stock2} - {name_stock1}")
# plt.title(f"Residuals from regression \n Residual = {name_stock2} - ({alpha:.2f} + {beta:.2f}*{name_stock1})", fontsize=10)
# plt.xlabel("Time")
# plt.ylabel("Values")
# plt.legend()
# plt.show


# Dickey-Fuller test
# use pandas to output results nicely
dftest = adfuller(errors, maxlag=1)
dfoutput = pd.Series(dftest[0:4], index=["Test statistic", "p-value", "Number of lags used", "Number of observations used",]) #https://www.statsmodels.org/dev/generated/statsmodels.tsa.stattools.adfuller.html
critical_values = pd.Series(dftest[4].values(), index=dftest[4].keys())
print(f"Dickey Fuller results: \n{dfoutput} \n\nDicky Fuller critical values:\n{critical_values}")

# For x, y to be cointegrated the error in the linear regression must be stationary. 
# The error is stationary <-> the error is not integrated (its order of integration is I(0))
# Dickey-Fuller tests whether a series is integrated (with the null hypothesis being that it is integrated)
# We want the error to be stationary. So we want to reject the null hypothesis that the error is integrated.
# We reject the null hypothesis if the test statistic is more negative than the critical value (for a given confidence level).
# We have a test statistic of -3.108, this is more negative than the critical value at the 5% and 10% confidence levels but not 
# at the 1% confidence level. So at 5% and 10%, we can reject the null hypthesis. 
# So, at 5% and 10%, the error is not integrated. x and y are cointegrated (at 5% and 10% confidence level). 
#
# If we cannot reject the null hypothesis we stop since we have not detected cointegration between x and y.


# z-score to determine entry and exit points
# z-score: how many standard deviations away from the mean a data point is (here, data point=error at time t)
zscore = (errors - np.mean(errors))/np.std(errors)
zscore.plot(label="z-score")
plt.title(f"z-score {name_stock2}-{name_stock1}")
plt.xlabel("Time")
plt.ylabel("z-score value")
u_threshold = 1.2
l_threshold = -1.2
plt.axhline(y=u_threshold, color="b", label=f"{u_threshold} threshold")
plt.axhline(y=l_threshold, color="b", label=f"{l_threshold} threshold")
plt.legend()
plt.show()


# Entry and exit rules
signal_short_entry = u_threshold
signal_long_entry = l_threshold
signal_exit = 0
btest = pd.DataFrame()
btest["stock2"] = stock2_data["Close"]
btest["stock1"] = stock1_data["Close"]
btest["short signal"] = (zscore > signal_short_entry) & (zscore.shift(1) < signal_short_entry) # zscore exceeds upper threshold from below 
btest["short exit"] = (zscore < signal_exit) & (zscore.shift(1) > signal_exit) # zscore falls below exit level (0) from above
btest["long signal"] = (zscore < signal_long_entry) & (zscore.shift(1) > signal_long_entry)
btest["long exit"] = (zscore > signal_exit) & (zscore.shift(1) < signal_exit)


# generate the backtest
spread_side = None
counter = -1 
backtest_result = []
for time, signals_stock in btest.iterrows():
    counter+=1 
    # unpack the list signals_stock (corresponds to a row of the btest dataframe) and make six variables
    stock2_, stock1_, short_signal, short_exit, long_signal, long_exit = signals_stock
    
    if spread_side == None:
        return_stock2 = 0
        return_stock1 = 0
        backtest_result.append([time, return_stock2, return_stock1, spread_side])
        
        if short_signal == True:
            spread_side = "short"
        elif long_signal == True:
            spread_side = "long"
            
    elif spread_side == "long":
        return_stock2 = btest["stock2"][counter] / btest["stock2"][counter-1] -1
        return_stock1 = btest["stock1"][counter] / btest["stock1"][counter-1] -1
        backtest_result.append([time, return_stock2, -return_stock1, spread_side])
        
        if long_exit == True:
            spread_side = None
    
    elif spread_side == "short":
        return_stock2 = btest["stock2"][counter] / btest["stock2"][counter-1] -1
        return_stock1 = btest["stock1"][counter] / btest["stock1"][counter-1] -1
        backtest_result.append([time, -return_stock2, return_stock1, spread_side])
        
        if short_exit == True:
            spread_side = None 
        
    
# put backtest_result into a data frame and calculate the cumulative profit/losses
backtest_pandas = pd.DataFrame(backtest_result)
backtest_pandas.columns = ["Date", "stock2", "stock1", "Side"]
backtest_pandas["stock2 PL"] = np.cumprod(backtest_pandas["stock2"] + 1)
backtest_pandas["stock1 PL"] = np.cumprod(backtest_pandas["stock1"] + 1)
backtest_pandas["Total PL"] = (backtest_pandas["stock1 PL"] + backtest_pandas["stock2 PL"]) / 2
backtest_pandas.index = backtest_pandas["Date"]


# plot the PL
backtest_pandas[["Total PL"]].plot(label = "Profit and loss")
plt.title("Equity Curve Pairs Trading")
plt.xlabel("Time")
plt.ylabel("Values")
plt.legend()
plt.show()



# 1. Set up linear regression between the two instruments
# 2. run Dickey-Fuller test on the error terms from the linear regression (test whether error is stationary)
#    if error is stationary continue to 3.
# 3. use z-score of error to generate entry and exit signals for the instruments: if error is more than a threshold
#    level past its mean, buy or sell the corresponding stock

# Criticism: 
# - beta (from the linear regression) can change
# - ADF test can lead to rejecting the pair, even if trading them would have yielded high return.
#   e.g. AMD and Intel: ADF null hypothesis is not rejected but trading anyway based on z-score gives a PL of 5, 
#   basically driven by AMD's extreme performance
# - shorting a stock is not always viable 
# - z-value threshold level is arbitrary (data snooping bias!)






















