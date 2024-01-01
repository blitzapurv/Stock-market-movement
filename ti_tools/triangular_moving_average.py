from __future__ import absolute_import
from ti_tools import catch_errors
from ti_tools.simple_moving_average import (
    simple_moving_average as sma
    )


def triangular_moving_average(data, period):
    """
    Triangular Moving Average.

    Formula:
    TMA = SMA(SMA())
    """
    catch_errors.check_for_period_error(data, period)

    tma = sma(sma(data, period), period)
    return tma
