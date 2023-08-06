Change Log
**********

These are the enhancements, breaking changes and bug fixes of note between each
release.

.. _v0.3.0:

`0.3.0`_ - 2023-04-16
=====================

.. _0.3.0: https://gitlab.com/signalytics/signalyzer/compare/v0.2.4..._v0.3.0:

Enhancements
------------

* Add method :meth:`~Trace.alpha_beta_filter` to filter a measured signal with
  an alpha-beta filter.
* Add dataclass :class:`AlphaBetaFilterTraces` for the trace collection produced
  by an alpha-beta filter.
* Add dataclass :class:`AlphaBetaFilter` for the results produced by the
  alpha-beta filter.
* Add :attr:`~VectorTraces.delta_phi` trace to the vector trace collection.
* Upgrade type hints to new convention.


Breaking Changes
----------------

* Drop support for Python 3.9.

.. _v0.2.4:

`0.2.4`_ - 2022-03-15
=====================

.. _0.2.4: https://gitlab.com/signalytics/signalyzer/compare/v0.2.3...v0.2.4

Enhancements
------------

* Add method :meth:`~Trace.moving_events` to count the occurrences of an event
  in form of a sample value within a moving window over the samples.
* Add method :meth:`~Trace.fmod` to modulo divide the signal samples.

.. _v0.2.3:

`0.2.3`_ - 2022-03-06
=====================

.. _0.2.3: https://gitlab.com/signalytics/signalyzer/compare/v0.2.2...v0.2.3

Enhancements
------------

* Add function :func:`logical_and` to logical AND a variable number of measured
  signals.
* Add function :func:`logical_or` to logical OR a variable number of measured
  signals.
* Add function :func:`priority` to prioritize a variable number of binary
  measured signals with a priority encoder.

.. _v0.2.2:

`0.2.2`_ - 2022-01-30
=====================

.. _0.2.2: https://gitlab.com/signalytics/signalyzer/compare/v0.2.1...v0.2.2

Enhancements
------------

* Add method :meth:`~Trace.interpolate` to piecewise linear interpolate a
  measured signal between data points.
* Add method :meth:`~Trace.delay` to delay (limit/filter) state changes of a
  binary measured signal by number of samples (binary change-rate limiter).

.. _v0.2.1:

`0.2.1`_ - 2022-01-27
=====================

.. _0.2.1: https://gitlab.com/signalytics/signalyzer/compare/v0.2.0...v0.2.1

Enhancements
------------

* Add method :meth:`~Statemachine.flowchart` to display the state transitions
  of a statemachine with a sankey flow-chart plot.

.. _v0.2.0:

`0.2.0`_ - 2022-01-18
=====================

.. _0.2.0: https://gitlab.com/signalytics/signalyzer/compare/v0.1.0...v0.2.0

Enhancements
------------

* Add method :meth:`~Trace.ramp` to limit the slew-rates of a measured signal.
* Add method :meth:`~Trace.slew` to process a measured signal with a
  slew-rate limiter.
* Add dataclass :class:`SlewRateLimiterTraces` for the trace collection produced
  by the slew-rate limiter.
* Add dataclass :class:`SlewRateLimiter` for the results produced by the
  slew-rate limiter.
* Add method :meth:`~Trace.pt1` to process a measured signal with the transfer
  function of a PT1-element.
* Add method :meth:`~Trace.dt1` to process a measured signal with the transfer
  function of a DT1-element.
* Add method :meth:`~Trace.figure` to create a figure with the scatter plot of
  the trace.

Breaking Changes
----------------

* Remove method :meth:`~Trace.lag` in favour of the new method :meth:`~Trace.pt1`.

.. _v0.1.0:

`0.1.0`_ - 2022-01-15
=====================

.. _0.1.0: https://gitlab.com/signalytics/signalyzer/compare

* First release.
