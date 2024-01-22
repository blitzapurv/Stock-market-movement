from __future__ import absolute_import
import numpy as np
from ti_tools import catch_errors
from ti_tools.function_helper import fill_for_noncomputable_vals
from ti_tools.simple_moving_average import (
    simple_moving_average as sma
    )
from six.moves import range

# %K = (Current Close - Lowest Low)/(Highest High - Lowest Low) * 100
# %D = 3-day SMA of %K

# Fast Stochastic Oscillator:
## Fast %K = %K basic calculation
## Fast %D = 3-period SMA of Fast %K

# Slow Stochastic Oscillator:
## Slow %K = Fast %K smoothed with 3-period SMA
## Slow %D = 3-period SMA of Slow %K

# Full Stochastic Oscillator:   (customizable version of slow stochastic oscillator)
## Full %K = Fast %K smoothed with X-period SMA
## Full %D = X-period SMA of Full %K
## Deafaut: (14,3,3)

def percent_k(data, period):
    """
    %K.

    Formula:
    %k = data(t) - low(n) / (high(n) - low(n))
    """
    catch_errors.check_for_period_error(data, period)
    percent_k = [((data[idx] - np.min(data[idx+1-period:idx+1])) /
         (np.max(data[idx+1-period:idx+1]) -
          np.min(data[idx+1-period:idx+1]))) for idx in range(period-1, len(data))]
    percent_k = fill_for_noncomputable_vals(data, percent_k)

    return percent_k


def percent_d(p_k, period=3):
    """
    %D.

    Formula:
    %D = SMA(%K, 3)
    """
    percent_d = sma(p_k, period)
    return percent_d
