.. currentmodule:: signalyzer

.. _signal processing:

Signal Processing
=================

The :class:`Trace` class has *methods* for `signal processing`_  the
:attr:`~Trace.samples` of a :class:`Trace`.

.. toctree::
   :maxdepth: 3
   :caption: Signal Processing
   :hidden:

   clipping
   change-rate-limiting
   slew-rate-limiting
   slew-rate-limiter
   iir-filters
   logic-functions
   pt1-element
   dt1-element
   alpha-beta-filter
   exponential-smoothing
   window-generator
   moving-events
   moving-differentiation
   moving-averages
   moving-linear-regression

Clipping
--------

.. csv-table::
   :header: "Method", "Name", "Label"
   :widths: 20, 80, 20
   :align: left

   :meth:`~Trace.clip`, :ref:`Clip <clip>`, ``'clip'``
   :meth:`~Trace.clamp`, :ref:`Clamp <clamp>`, ``'clamp'``

Rate Limiting
-------------

.. csv-table::
   :header: "Method", "Name", "Label"
   :widths: 20, 80, 20
   :align: left

   :meth:`~Trace.delay`, :ref:`Change-Rate Limiting <change-rate limiting>`, ``'delay'``
   :meth:`~Trace.ramp`, :ref:`Slew-Rate Limiting <slew-rate limiting>`, ``'ramp'``
   :meth:`~Trace.slew`, :ref:`Slew-Rate Limiter <slew-rate limiter>`, ``'slew'``

Filtering
---------

.. csv-table::
   :header: "Method", "Name", "Label"
   :widths: 20, 55, 20
   :align: left

   :meth:`~Trace.band_pass`, :ref:`Band-Pass filter <band-pass>`, ``'band-pass'``
   :meth:`~Trace.low_pass`, :ref:`Low-Pass filter <low-pass>`, ``'low-pass'``
   :meth:`~Trace.high_pass`, :ref:`High-Pass filter <high-pass>`, ``'high-pass'``
   :meth:`~Trace.notch`, :ref:`Notch filter <notch>`, ``'notch'``
   :meth:`~Trace.all_pass`, :ref:`All-Pass filter <all-pass>`, ``'all-pass'``

Logic Functions
---------------

.. csv-table::
   :header: "Method", "Name", "Label"
   :widths: 20, 80, 20
   :align: left

   :func:`all`, :ref:`All Samples True <all samples true>`,
   :func:`any`, :ref:`Any Sample True <any sample true>`,
   :func:`logical_and`, :ref:`Logical AND <logical and>`, ``'And'``
   :func:`logical_or`, :ref:`Logical OR <logical or>`, ``'Or'``
   :func:`priority`, :ref:`Priority Encoder <priority encoder>`, ``'Priority'``

Control Elements
----------------

.. csv-table::
   :header: "Method", "Name", "Label"
   :widths: 20, 80, 20
   :align: left

   :meth:`~Trace.pt1`, :ref:`PT1-element <pt1 element>`, ``'pt1'``
   :meth:`~Trace.dt1`, :ref:`DT1-element <dt1 element>`, ``'dt1'``

Smoothing
---------

.. csv-table::
   :header: "Method", "Name", "Label"
   :widths: 20, 80, 20
   :align: left

   :meth:`~Trace.alpha_beta_filter`, :ref:`Alpha-Beta Filter <alpha-beta filter>`, ``'filter'``
   :meth:`~Trace.exponential`, :ref:`Exponential smoothing <exponential smoothing>`, ``'exponential'``

Moving Window Functions
-----------------------

.. csv-table::
   :header: "Method", "Name", "Label"
   :widths: 20, 80, 20
   :align: left

   :meth:`~Trace.window`, :ref:`Moving window generator <moving window>`,
   :meth:`~Trace.moving_events`, :ref:`Moving event counter <moving event counter>`,  ``'events'``
   :meth:`~Trace.moving_differential`, :ref:`Moving differentiation <moving differentiation>`,  ``'differential'``
   :meth:`~Trace.moving_average`, :ref:`Moving averages <moving average>`, ``'average'``
   :meth:`~Trace.moving_regression`, :ref:`Moving linear regression <moving linear regression>`,  ``'regression'``
