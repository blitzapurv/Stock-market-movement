import numpy as np
import pandas as pd
import pandas_ta as ta
from backtesting import Strategy
from backtesting.lib import crossover
from ti_tools.simple_moving_average import simple_moving_average as sma
from ti_tools.relative_strength_index import relative_strength_index as rsi
from ti_tools.moving_average_convergence_divergence import (moving_average_convergence_divergence, 
                                                            signal_line, 
                                                            macd_histogram)


class MACDandRSI(Strategy):
    # define MACD, signal lengths
    fast_length = 12
    slow_length = 26
    signal_length = 9
    # define RSI bounds and length
    rsi_window = 14
    upper_bound = 70
    lower_bound = 30

    _props = f"{fast_length}_{slow_length}_{signal_length}"
    _temp_buying_posi = np.inf

    def init(self):
        # print(self._props)
        self.macd = self.I(moving_average_convergence_divergence, self.data.Close, short_period=self.fast_length, long_period=self.slow_length)
        self.signal = self.I(signal_line, self.macd, period=self.signal_length)
        self.rsi = self.I(rsi, pd.Series(self.data.Close), period=self.rsi_window)
    # sell everything if signal moves above macd and buy if it's vica-versa
    def next(self):
        if crossover(self.macd, self.signal) and (self.rsi[-1]<self.lower_bound):
            self.position.close()
            self.buy()
            # print("buying position :", self.data.Close[-1])
            self._temp_buying_posi = self.data.Close[-1]
        elif crossover(self.signal, self.macd) and (self.rsi[-1]>self.upper_bound):
            self.position.close()