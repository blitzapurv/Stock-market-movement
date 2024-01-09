from __future__ import absolute_import
from ti_tools import catch_errors
from ti_tools.exponential_moving_average import (
    exponential_moving_average as ema
    )


def moving_average_convergence_divergence(data, short_period=12, long_period=26):
    """
    Moving Average Convergence Divergence.

    Formula:
    EMA(DATA, P1) - EMA(DATA, P2)
    """
    catch_errors.check_for_period_error(data, short_period)
    catch_errors.check_for_period_error(data, long_period)

    macd = ema(data, short_period) - ema(data, long_period)
    return macd

def signal_line(data, period=9):
    """
    Signal Line: 9-day EMA of MACD
    """
    catch_errors.check_for_period_error(data, period)
    signal = ema(data, period)
    return signal

def macd_histogram(macd, signal):
    """
    MACD Histogram: MACD - Signal Line
    """
    return macd - signal