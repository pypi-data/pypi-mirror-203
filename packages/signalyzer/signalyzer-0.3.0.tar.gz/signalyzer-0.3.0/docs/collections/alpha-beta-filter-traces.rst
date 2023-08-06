.. currentmodule:: signalyzer

.. testsetup:: *

    from signalyzer import *

.. _alpha-beta filter trace:

Alpha-Beta Filter Traces
========================

The `alpha-beta filter trace`_ collection is used to store the resulting
:ref:`signal traces <signal trace>` produced by the
:ref:`alpha-beta filter <alpha-beta filter>` of the signal
:attr:`~Trace.samples` of a :ref:`signal trace <signal trace>`.

Create the Trace Collection
---------------------------

You can create an `alpha-beta filter trace`_ collection without
:attr:`~Trace.samples` by calling the :class:`AlphaBetaFilterTraces` class.

  >>> # create an empty alpha-beta filter trace collection
  >>> traces = AlphaBetaFilterTraces()
  >>> traces
  AlphaBetaFilterTraces(forecast=Trace(label='Trace', samples=[]),
                        forecast_sign=Trace(label='Trace', samples=[]),
                        level=Trace(label='Trace', samples=[]),
                        level_sign=Trace(label='Trace', samples=[]),
                        trend=Trace(label='Trace', samples=[]),
                        trend_sign=Trace(label='Trace', samples=[]),
                        trend_inflection=Trace(label='Trace', samples=[]),
                        error=Trace(label='Trace', samples=[]),
                        variance_forecast=Trace(label='Trace', samples=[]),
                        variance_level=Trace(label='Trace', samples=[]),
                        variance_trend=Trace(label='Trace', samples=[]))

Number of Traces
----------------

You can get the number of the traces in the :class:`AlphaBetaFilterTraces`
collection with the built-in function :func:`len`.

  >>> # number of traces in the collection
  >>> len(traces)
  11

Names of the Traces
-------------------

You can get the :class:`list` with the names of the traces in the
:class:`AlphaBetaFilterTraces` collection.

A :class:`list` with the key names of the traces is returned.

  >>> # key names of the traces in the collection
  >>> list(traces)
  ['forecast',
   'forecast_sign',
   'level',
   'level_sign',
   'trend',
   'trend_sign',
   'trend_inflection',
   'error',
   'variance_forecast',
   'variance_level',
   'variance_trend']

  >>> # key names of the traces in the collection
  >>> list(traces.keys())
  ['forecast',
   'forecast_sign',
   'level',
   'level_sign',
   'trend',
   'trend_sign',
   'trend_inflection',
   'error',
   'variance_forecast',
   'variance_level',
   'variance_trend']

Forecast Trace
--------------

You can get the *forecast* :class:`Trace` with the
:attr:`~AlphaBetaFilterTraces.forecast` attribute from the
:class:`AlphaBetaFilterTraces` collection.

The :class:`Trace` with the *forecast* :attr:`~Trace.samples` is returned.

  >>> # forecast trace by attribute
  >>> traces.forecast
  Trace(label='Trace', samples=[])
  >>> # forecast trace by key
  >>> traces['forecast']
  Trace(label='Trace', samples=[])

Forecast Sign Trace
-------------------

You can get the *forecast sign* :class:`Trace` with the
:attr:`~AlphaBetaFilterTraces.forecast_sign` attribute from the
:class:`AlphaBetaFilterTraces` collection.

The :class:`Trace` with the *forecast sign* :attr:`~Trace.samples` is returned.

  >>> # forecast sign trace by attribute
  >>> traces.forecast_sign
  Trace(label='Trace', samples=[])
  >>> # forecast trace by key
  >>> traces['forecast_sign']
  Trace(label='Trace', samples=[])

Level Trace
-----------

You can get the *level* :class:`Trace` with the
:attr:`~AlphaBetaFilterTraces.level` attribute from the
:class:`AlphaBetaFilterTraces` collection.

The :class:`Trace` with the *level* :attr:`~Trace.samples` is returned.

  >>> # level trace by attribute
  >>> traces.level
  Trace(label='Trace', samples=[])
  >>> # level trace by key
  >>> traces['level']
  Trace(label='Trace', samples=[])

Level Sign Trace
----------------

You can get the *level sign* :class:`Trace` with the
:attr:`~AlphaBetaFilterTraces.level_sign` attribute from the
:class:`AlphaBetaFilterTraces` collection.

The :class:`Trace` with the *level* :attr:`~Trace.samples` is returned.

  >>> # level sign trace by attribute
  >>> traces.level_sign
  Trace(label='Trace', samples=[])
  >>> # level sign trace by key
  >>> traces['level_sign']
  Trace(label='Trace', samples=[])

Trend Trace
-----------

You can get the *trend* :class:`Trace` with the
:attr:`~AlphaBetaFilterTraces.trend` attribute from the
:class:`AlphaBetaFilterTraces` collection.

The :class:`Trace` with the *trend* :attr:`~Trace.samples` is returned.

  >>> # trend trace by attribute
  >>> traces.trend
  Trace(label='Trace', samples=[])
  >>> # trend trace by key
  >>> traces['trend']
  Trace(label='Trace', samples=[])

Trend Sign Trace
----------------

You can get the *trend sign* :class:`Trace` with the
:attr:`~AlphaBetaFilterTraces.trend_sign` attribute from the
:class:`AlphaBetaFilterTraces` collection.

The :class:`Trace` with the *trend sign* :attr:`~Trace.samples` is returned.

  >>> # trend sign trace by attribute
  >>> traces.trend_sign
  Trace(label='Trace', samples=[])
  >>> # trend sign trace by key
  >>> traces['trend_sign']
  Trace(label='Trace', samples=[])

Trend Inflection Trace
----------------------

You can get the *trend inflection* :class:`Trace` between the predicted
*forecast* and the estimated *level* with the
:attr:`~AlphaBetaFilterTraces.trend_inflection` attribute from the
:class:`AlphaBetaFilterTraces` collection.

The :class:`Trace` with the *trend sign* :attr:`~Trace.samples` is returned.

  >>> # trend sign trace by attribute
  >>> traces.trend_inflection
  Trace(label='Trace', samples=[])
  >>> # trend sign trace by key
  >>> traces['trend_inflection']
  Trace(label='Trace', samples=[])

Error Trace
-----------

You can get the *error* :class:`Trace` for the predicted *forecast*
with the :attr:`~AlphaBetaFilterTraces.error` attribute from the
:class:`AlphaBetaFilterTraces` collection.

The :class:`Trace` with the *error* :attr:`~Trace.samples` is returned.

  >>> # error trace by attribute
  >>> traces.error
  Trace(label='Trace', samples=[])
  >>> # error trace by key
  >>> traces['error']
  Trace(label='Trace', samples=[])

Variance Reduction Factors
--------------------------

Forecast Trace
~~~~~~~~~~~~~~

You can get the *variance* **reduction factor** for the *forecast* :class:`Trace`
with the :attr:`~AlphaBetaFilterTraces.variance_forecast` attribute from the
:class:`AlphaBetaFilterTraces` collection.

The :class:`Trace` with the *forecast variance* reduction factor
:attr:`~Trace.samples` is returned.

  >>> # variance reduction factor forecast trace by attribute
  >>> traces.variance_forecast
  Trace(label='Trace', samples=[])
  >>> # variance reduction factor forecast trace by key
  >>> traces['variance_forecast']
  Trace(label='Trace', samples=[])

Level Trace
~~~~~~~~~~~

You can get the *variance* **reduction factor** for the *level* :class:`Trace`
with the :attr:`~AlphaBetaFilterTraces.variance_level` attribute from the
:class:`AlphaBetaFilterTraces` collection.

The :class:`Trace` with the *variance* **reduction factor** :attr:`~Trace.samples`
for the *level* :class:`Trace` is returned.

  >>> # variance reduction factor level trace by attribute
  >>> traces.variance_level
  Trace(label='Trace', samples=[])
  >>> # level variance reduction level trace by key
  >>> traces['variance_level']
  Trace(label='Trace', samples=[])

Trend Trace
~~~~~~~~~~~

You can get the *variance* **reduction factor** for the *trend* :class:`Trace`
with the :attr:`~AlphaBetaFilterTraces.variance_trend` attribute from the
:class:`AlphaBetaFilterTraces` collection.

The :class:`Trace` with the *variance* **reduction factor** :attr:`~Trace.samples`
for the *trend* :class:`Trace` is returned.


  >>> # variance reduction factor trend trace by attribute
  >>> traces.variance_trend
  Trace(label='Trace', samples=[])
  >>> # variance reduction factor trend trace by key
  >>> traces['variance_trend']
  Trace(label='Trace', samples=[])

