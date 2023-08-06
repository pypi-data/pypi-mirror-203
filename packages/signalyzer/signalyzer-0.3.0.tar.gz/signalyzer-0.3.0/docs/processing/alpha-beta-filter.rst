.. currentmodule:: signalyzer

.. testsetup:: *

    from signalyzer import *

.. _alpha-beta filter:

Alpha-Beta Filter
=================

The signal :attr:`~Trace.samples` of a :ref:`signal trace <signal trace>` can be
processed with an `alpha-beta filter`_.

Create the Trace Collection
---------------------------

You can smooth the signal :attr:`~Trace.samples` with an `alpha-beta filter`_
by calling the method :meth:`~Trace.alpha_beta_filter`.

An :ref:`alpha-beta filter trace <alpha-beta filter trace>` collection is
returned.

  >>> # filter the signal samples
  >>> traces = Trace('Signal', [1, 2, 3]).alpha_beta_filter(dt=1, alpha=0.5, beta=1)
  >>> traces
  AlphaBetaFilterTraces(forecast=Trace(label='Signal:filter:forecast',
                        samples=[1.0, 1.0, 2.5]),
    forecast_sign=Trace(label='Signal:filter:forecast_sign',
                        samples=[1.0, 1.0, 1.0]),
    level=Trace(label='Signal:filter:level',
                samples=[1.0, 1.5, 2.75]),
    level_sign=Trace(label='Signal:filter:level_sign',
                     samples=[1.0, 1.0, 1.0]),
    trend=Trace(label='Signal:filter:trend',
                samples=[0.0, 1.0, 1.5]),
    trend_sign=Trace(label='Signal:filter:trend_sign',
                     samples=[0.0, 1.0, 1.0]),
    trend_inflection=Trace(label='Signal:filter:trend_inflection',
                           samples=[0.0, 1.0, 1.0]),
    error=Trace(label='Signal:filter:error',
                samples=[0.0, 1.0, 0.5]),
    variance_forecast=Trace(label='Signal:filter:variance_forecast',
                            samples=[3.0, 3.0, 3.0]),
    variance_level=Trace(label='Signal:filter:variance_level',
                         samples=[1.0, 1.0, 1.0]),
    variance_trend=Trace(label='Signal:filter:variance_trend',
                         samples=[2.0, 2.0, 2.0]))

.. note::

  The `alpha-beta filter`_ uses the first signal sample as the initial *level*,
  and the initial *trend* is set by default to zero.

Figure
------

You can visualize the trace collection with a figure containing the subplots of
the traces in the collection by calling the method
:meth:`~AlphaBetaFilterTraces.figure`.

  >>> figure = Trace('Signal', range(20)).alpha_beta_filter(1, 0.5, 1).figure()

.. plotly::

  from signalyzer import Trace

  signal = Trace('Signal', range(20))
  traces = signal.alpha_beta_filter(1, 0.5, 1.0)
  fig = traces.figure(original=signal)

  fig.show()
