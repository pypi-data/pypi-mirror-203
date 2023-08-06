.. _NumPy: https://numpy.org/doc/stable/
.. _pandas: https://pandas.pydata.org/docs

.. currentmodule:: signalyzer

.. testsetup:: *

    from signalyzer import *

Trace Conversions
=================

Convert Trace to Dictionary
---------------------------

Your can convert a :class:`Trace` into a :class:`dict` class by calling the
method :meth:`~Trace.as_dict`.

  >>> Trace('Signal', [1, 2, 3]).as_dict()
  {'label': 'Signal', 'samples': [1, 2, 3]}

Your can convert a :class:`Trace` into a :class:`dict` class with the
function :func:`~dataclasses.asdict` from the :mod:`dataclasses` module.

  >>> from dataclasses import asdict
  >>> asdict(Trace('Signal', [1, 2, 3]))
  {'label': 'Signal', 'samples': [1, 2, 3]}

Convert Trace to Tuple
----------------------

You can convert a :class:`Trace` into a :class:`tuple` class by calling the
method :meth:`~Trace.as_tuple`.

  >>> Trace('Signal', [1, 2, 3]).as_tuple()
  ('Signal', [1, 2, 3])

Your can convert a :class:`Trace` into a :class:`tuple` class with the
function :func:`~dataclasses.astuple` from the :mod:`dataclasses` module.

  >>> from dataclasses import astuple
  >>> astuple(Trace('Signal', [1, 2, 3]))
  ('Signal', [1, 2, 3])

Convert Trace to List
---------------------

You can convert a :class:`Trace` into a :class:`list` class.

  >>> list(Trace('Signal', [1, 2, 3]))
  [1, 2, 3]

Convert Trace to `NumPy`_ Array
-------------------------------

You can convert a :class:`Trace` into a :class:`~numpy.ndarray` class.

  >>> import numpy as np
  >>> np.array(Trace('Signal', [0, False, 1, True, np.pi]))
  array([0.        , 0.        , 1.        , 1.        , 3.14159265])

Convert Trace to `Pandas`_ Series
---------------------------------

You can convert a :class:`Trace` into a :class:`~pandas.Series` class.

  >>> import pandas as pd
  >>> pd.Series(Trace('Signal', [0, False, 1, True, np.pi]))
  0           0
  1       False
  2           1
  3        True
  4    3.141593
  dtype: object
