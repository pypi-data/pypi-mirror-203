.. currentmodule:: signalyzer

.. _JupyterLab: https://jupyter.org/
.. _numpy: https://numpy.org/
.. _scipy: https://www.scipy.org/
.. _pandas: https://pandas.pydata.org/docs/
.. _plotly: https://plotly.com/python/
.. _dash: https://dash.plotly.com/
.. _streamlit: https://streamlit.io/
.. _voila: https://voila.readthedocs.io/
.. _PyPI package registry: https://gitlab.com/signalytics/signalyzer/-/packages
.. _PyPI: https://pypi.org/project/signalyzer

.. |status| image:: https://img.shields.io/pypi/status/signalyzer.svg
   :target: https://pypi.org/project/signalyzer
.. |docs| image:: https://readthedocs.org/projects/signalyzer/badge/?version=latest
   :target: https://signalyzer.readthedocs.io
.. |pypi| image:: https://img.shields.io/pypi/v/signalyzer.svg
   :target: https://pypi.org/project/signalyzer
.. |python| image:: https://img.shields.io/pypi/pyversions/signalyzer.svg
   :target: https://docs.python.org/3
.. |license| image:: https://img.shields.io/pypi/l/signalyzer.svg
   :target: https://gitlab.com/signalytics/signalyzer/-/blob/main/LICENSE
.. |downloads| image:: https://img.shields.io/pypi/dm/signalyzer.svg
   :target: https://pypistats.org/packages/signalyzer
.. |binder| image:: https://mybinder.org/badge_logo.svg
   :target: https://mybinder.org/v2/gl/signalytics%2Fsignalyzer/main?labpath=notebooks

|status| |docs| |pypi| |python| |license| |downloads|

Welcome to the Signalyzer Documentation
=======================================

|binder|

**signalyzer** is a Python package to analyze and process time-discrete,
equidistant measured signals, and visualize them with the open source `Plotly`_
library for Python.

Main features of the **signalyzer** package are

* transform and combine measured signals into a new one
* descriptive statistics over the measured signal
* interactive plotting of the measured signal with `Plotly`_
* integrating (accumulating) of the measured signal
* differentiating of the measured signal
* clipping of the measured signal
* rate limiting of the measured signal
* filtering of the measured signal
* logical operations between measured signals
* prioritizing measured logic signals with a priority encoder
* smoothing of the measured signal with statistics
* process measured signals with a moving window
* moving sample value (event) counter
* moving averages with window statistics
* moving differentiation
* moving OLS linear regression with window statistics
* shifting (moving) of the measured signal
* slicing of the measured signal
* evaluate statemachine transitions observed by measured state signal

.. important::

  The ``signalyzer`` package is best used within the `JupyterLab`_ web-based
  interactive development environment for Jupyter notebooks or with Plotly
  `Dash`_, `Streamlit`_  or Jupyter `voila`_ to build standalone web applications
  and dashboards.

Dependencies
------------

The **signalyzer** package runs on `Python 3.10 <https://www.python.org>`_ or
higher, and depends on the external packages

* `numpy`_ for mathematical computations
* `scipy`_ for signal processing and signal statistics computations
* `pandas`_ for data import and statistic computations
* `plotly`_ for visualizations

Installation
------------

You can get the latest *version* of the **signalyzer** package directly from the
`PyPI package registry`_ on GitLab:

  `Signalyzer @ gitlab <https://gitlab.com/signalytics/signalyzer/>`_

You can get the latest *release* of the **signalyzer** package directly from
`PyPI`_:

.. code-block:: shell

  pip install signalyzer

Modules
-------

The ``signalyzer`` package comes with two modules.

The :ref:`trace module <signal trace>` for transforming, processing, analyzing
and plotting time-discrete, equidistant signals.

.. note::

  The ``signalyzer.trace`` module is imported into the package namespace.

The :ref:`statemachine module <statemachine>` for evaluating and plotting state
transitions of a state machine observed by a time-discrete, equidistant signal.

.. note::

  The ``signalyzer.statemachine`` module is imported into the package namespace.


.. toctree::
   :caption: Trace
   :maxdepth: 3
   :hidden:

   trace/index
   transformations/index
   collections/index
   processing/index

.. toctree::
   :caption: State Machines
   :maxdepth: 3
   :hidden:

   statemachine/index

.. toctree::
   :caption: References
   :maxdepth: 4
   :hidden:

   api/index

.. toctree::
   :caption: Annex
   :maxdepth: 2
   :hidden:

   annex/changelog
   annex/license
   annex/contributing

.. toctree::
   :caption: Indexes
   :maxdepth: 1
   :hidden:

   genindex
