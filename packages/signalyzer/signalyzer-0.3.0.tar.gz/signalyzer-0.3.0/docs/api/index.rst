API
***

This part of the documentation lists the full API reference of all public
classes and functions.

.. currentmodule:: signalyzer

Type Hints Support
==================

.. autoclass:: Number

.. autoclass:: Sample

.. autoclass:: Samples

.. autoclass:: Operand

.. autoclass:: DataFrame

Signal Traces
=============

Trace
-----

.. autoclass:: Trace
   :members:

vectorize
~~~~~~~~~

.. autofunction:: vectorize

Logic Functions
---------------

Logical AND
~~~~~~~~~~~

.. autofunction:: logical_and

Logical OR
~~~~~~~~~~

.. autofunction:: logical_or

Priority Encoder
~~~~~~~~~~~~~~~~

.. autofunction:: priority

Traces
------

.. autoclass:: Traces
   :members:

VectorTraces
------------

.. autoclass:: VectorTraces
   :members:

polar
~~~~~

.. autofunction:: polar

StatisticsTraces
----------------

.. autoclass:: StatisticsTraces
   :members:

MovingAverageTraces
-------------------

.. autoclass:: MovingAverageTraces
   :members:

SetTraces
---------

.. autoclass:: SetTraces
   :members:

combine
~~~~~~~

.. autofunction:: combine


SlewRateLimiterTraces
---------------------

.. autoclass:: SlewRateLimiterTraces
   :members:

ExponentialSmoothingTraces
--------------------------

.. autoclass:: ExponentialSmoothingTraces
   :members:

LinearRegressionTraces
----------------------

.. autoclass:: LinearRegressionTraces
   :members:

AlphaBetaFilterTraces
---------------------

.. autoclass:: AlphaBetaFilterTraces
   :members:

Representations
===============

2D-Point
--------

.. autoclass:: Point2D
   :members:

3D-Point
--------

.. autoclass:: Point3D
   :members:

Vector
------

.. autoclass:: Vector
   :members:

2D-State
--------

.. autoclass:: State2D
   :members:

3D-State
--------

.. autoclass:: State3D
   :members:


Signal Processing
=================

Statistics
----------

.. autoclass:: Statistics
   :members:

Slew-Rate Limiter
-----------------

.. autoclass:: SlewRateLimiter
   :members:

Exponential Smoothing
---------------------

.. autoclass:: ExponentialSmoothing
   :members:

Linear Regression
-----------------

.. autoclass:: LinearRegression
   :members:

Filtering
---------

.. autoclass:: AlphaBetaFilter
   :members:

.. autoclass:: IIRFilter
   :members:

State Machines
==============

Statemachine
------------

.. autoclass:: Statemachine
   :members:

Converters
==========

as_traces
---------

.. autofunction:: as_traces
