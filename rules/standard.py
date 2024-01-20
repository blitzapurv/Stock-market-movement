from backtesting import Strategy
from backtesting.lib import crossover
from ti_tools.simple_moving_average import simple_moving_average as sma
from ti_tools.relative_strength_index import relative_strength_index as rsi


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
        self.rsi = self.I(rsi, self.data.Close, self.rsi_window)

    # sell everything if rsi greater than upper bound and buy if it's lower than lower bound
    def next(self):
        if crossover(self.rsi, self.upper_bound):
            self.position.close()
            self.sell()
        elif crossover(self.lower_bound, self.rsi):
            self.position.close()
            self.buy()