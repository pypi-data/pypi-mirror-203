# -*- coding: utf-8 -*-
"""
signalyzer.py
~~~~~~~~~~~~~
Public package API.

:copyright: (c) 2021-2023 by Jochen Gerhaeusser.
:license: BSD, see LICENSE for details.
"""
from __future__ import annotations

from .trace import *
from .statemachine import *

# package exports
__all__ = [
    # Custom Types
    'Number',
    'Sample', 'Samples',
    'Operand',
    'DataFrame',

    # Representations
    'Point2D', 'Vector',
    'Point3D',
    'State2D', 'State3D',

    # Signal Processing
    'Statistics',
    'SlewRateLimiter',
    'ExponentialSmoothing',
    'LinearRegression',
    'IIRFilter',

    # State Machines
    'Statemachine',

    # Traces
    'Trace', 'vectorize',
    'logical_and', 'logical_or', 'priority',
    'Traces', 'as_traces',
    'VectorTraces', 'polar',
    'StatisticsTraces',
    'MovingAverageTraces',
    'SetTraces', 'combine',
    'SlewRateLimiterTraces',
    'AlphaBetaFilterTraces',
    'ExponentialSmoothingTraces',
    'LinearRegressionTraces'
]

__version__ = '0.3.0'
