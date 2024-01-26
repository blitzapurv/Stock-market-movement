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



class MACDHistBars(Strategy):
    """A strategy that monitors the length of MACD histogram bars to decide buying and selling points.
    """
    # define MACD, signal lengths
    fast_length = 12
    slow_length = 26
    signal_length = 9
    # define RSI bounds and length
    rsi_window = 14
    upper_bound = 70
    lower_bound = 30
    # other parameters
    use_rsi = 1 #0,1,2
    buy_steps = 1
    sell_steps = 1

    _props = f"{fast_length}_{slow_length}_{signal_length}"

    def init(self):
        # print(self._props)
        self.macd = self.I(moving_average_convergence_divergence, self.data.Close, short_period=self.fast_length, long_period=self.slow_length, plot=False)
        self.signal = self.I(signal_line, self.macd, period=9, plot=False)
        self.histogram = self.I(macd_histogram, macd=self.macd, signal=self.signal)
        self.rsi = self.I(rsi, pd.Series(self.data.Close), period=self.rsi_window)
        
    def _bar_length_change(self, up:bool=True, n_steps=1):
        """
        Return `True` if `series1` consecutively increased 'n_steps' number of times.
        """
        series1 = (
            self.histogram.values if isinstance(self.histogram, pd.Series) else
            self.histogram)
        if up:
            try:
                return all(series1[-i] >= series1[-i-1] for i in range(1, n_steps+1))
            except IndexError:
                return False
        else:
            try:
                return all(series1[-i-1] >= series1[-i] for i in range(1, n_steps+1))
            except IndexError:
                return False

    # sell everything if signal moves above macd and buy if it's vica-versa
    def next(self):
        if self.use_rsi==0:
            if self._bar_length_change(True, n_steps=self.buy_steps) and (self.rsi[-1]<self.lower_bound):
                # self.position.close()
                self.buy()
            elif self._bar_length_change(False, n_steps=self.sell_steps) and (self.rsi[-1]>self.upper_bound):
                self.position.close()
        elif self.use_rsi==1:
            if self._bar_length_change(True, n_steps=self.buy_steps):
                # self.position.close()
                self.buy()
            elif self._bar_length_change(False, n_steps=self.sell_steps):
                self.position.close()
        elif self.use_rsi==2:
            if (self.rsi[-1]<self.lower_bound):
                # self.position.close()
                self.buy()
            elif self._bar_length_change(False, n_steps=self.sell_steps):
                self.position.close()