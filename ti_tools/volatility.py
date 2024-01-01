from __future__ import absolute_import
from ti_tools.standard_deviation import standard_deviation as sd
from ti_tools.standard_variance import standard_variance as sv


def volatility(data, period):
    """
    Volatility.

    Formula:
    SDt / SVt
    """
    volatility = sd(data, period) / sv(data, period)
    return volatility
