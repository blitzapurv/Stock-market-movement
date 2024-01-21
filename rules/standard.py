import pandas as pd
import pandas_ta as ta
from backtesting import Strategy
from backtesting.lib import crossover
from ti_tools.simple_moving_average import simple_moving_average as sma
from ti_tools.relative_strength_index import relative_strength_index as rsi
from ti_tools.moving_average_convergence_divergence import (moving_average_convergence_divergence, 
                                                            signal_line, 
                                                            macd_histogram)


class SmaCross(Strategy):
    # Define the two MA lags as *class variables*
    # for later optimization
    n1 = 10
    n2 = 25
    
    def init(self):
        # Precompute the two moving averages
        self.sma1 = self.I(sma, self.data.Close, self.n1)
        self.sma2 = self.I(sma, self.data.Close, self.n2)
    
    def next(self):
        # If sma1 crosses above sma2, close any existing
        # short trades, and buy the asset
        if crossover(self.sma1, self.sma2):
            self.position.close()
            self.buy()

        # Else, if sma1 crosses below sma2, close any existing
        # long trades, and sell the asset
        elif crossover(self.sma2, self.sma1):
            self.position.close()
            self.sell()


class RsiOscillator(Strategy):
    # define bounds and period 
    upper_bound = 70
    lower_bound = 30
    rsi_window = 14

    # Do as much initial computation as possible
    def init(self):
        self.rsi = self.I(ta.rsi, pd.Series(self.data.Close), length=self.rsi_window)

    # sell everything if rsi greater than upper bound and buy if it's lower than lower bound
    def next(self):
        if crossover(self.rsi, self.upper_bound):
            self.position.close()
        elif crossover(self.lower_bound, self.rsi):
            self.position.close()
            self.buy()


class MACDcross(Strategy):
    # define lengths 
    fast_length = 12
    slow_length = 26
    signal_length = 9
    _props = f"{fast_length}_{slow_length}_{signal_length}"
    # Do as much initial computation as possible
    def init(self):
        print(self._props)
        self.macd = self.I(moving_average_convergence_divergence, self.data.Close, short_period=self.fast_length, long_period=self.slow_length)
        self.signal = self.I(signal_line, self.macd, period=9)
    
    # sell everything if signal moves above macd and buy if it's vica-versa
    def next(self):
        if crossover(self.macd, self.signal):
            self.position.close()
            self.buy()
        elif crossover(self.signal, self.macd):
            self.position.close()