<div align="center">
  <img src="https://signalytics.gitlab.io/signalyzer/_static/images/signalyzer.svg"><br>
</div>

---

# Signalyzer

[![status](https://img.shields.io/pypi/status/signalyzer.svg)](https://pypi.org/project/signalyzer)
[![docs](https://readthedocs.org/projects/signalyzer/badge/?version=latest)](https://signalyzer.readthedocs.io)
[![pypi](https://img.shields.io/pypi/v/signalyzer.svg)](https://pypi.org/project/signalyzer)
[![python](https://img.shields.io/pypi/pyversions/signalyzer.svg)](https://docs.python.org/3/)
[![license](https://img.shields.io/pypi/l/signalyzer.svg)](https://gitlab.com/signalytics/signalyzer/-/blob/main/LICENSE)
[![downloads](https://img.shields.io/pypi/dm/signalyzer.svg)](https://pypistats.org/packages/signalyzer)
[![binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gl/signalytics%2Fsignalyzer/main?labpath=notebooks)

**signalyzer** is a Python package to analyze and process time-discrete,
equidistant measured signals, and visualize them with the open source
[Plotly](https://plotly.com/python/) library for [Python].

Main features of the **signalyzer** package are

* transform and combine measured signals into a new one
* descriptive statistics over the measured signal
* interactive plotting of the measured signal with [Plotly]
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

> **Important**: The **signalyzer** package is best used within [JupyterLab] a
> web-based interactive development environment for [Jupyter] notebooks or with
> Plotly [Dash], [Streamlit] or Jupyter [voila] to build standalone web
> applications and dashboards.

## Table of Contents
[Back to top]: #table-of-contents

1. [Project Status](#project-status)
2. [Project Structure](#project-structure)
3. [Getting Started](#getting-started)
	- [Dependencies](#dependencies)
	- [Installation](#installation)
	- [Usage](#usage)
4. [Development](#development)
	- [Getting the Source](#getting-the-source)
	- [Building a Distribution](#building-a-distribution)
	- [Building the Documentation](#building-the-documentation)
5. [Release Process](#release-process)
	- [Versioning](#versioning)
6. [Documentation](#documentation)
7. [Contributing](#contributing)
8. [License](#license)
9. [Authors](#authors)

## Project Status

This [project] is stable and active. Feedback is always welcomed!

**[Back to top](#table-of-contents)**

## Project Structure

The [project] is organized in sub-folders.

- `assets`: [Project] assets files
- `docs/`: [Sphinx] documentation
- `notebooks/`: [Jupyter] notebooks
- `src/signalyzer/`: Package sources
  - `signalyzer/trace`: Trace module sources
  - `signalyzer/statemachine`: Statemachine module sources

**[Back to top](#table-of-contents)**

## Getting Started

### Dependencies

The `signalyzer` package requires at least [Python] 3.10 and depends on the
external packages:

- [numpy]
- [scipy]
- [pandas]
- [plotly]

### Installation

The [project] can be installed from [PyPI] using [pip]

```shell
> pip install signalyzer
```

**[Back to top](#table-of-contents)**

### Usage

Please read the online documentation hosted on "[Read The Docs]".

**[Back to top](#table-of-contents)**

## Development

### Getting the Source

This [project] is hosted on [gitlab].
You can clone this [project] directly using this command:

```shell
> git clone https://gitlab.com/signalytics/signalyzer.git
```

### Building a Distribution

To build a distribution of this [project] local, use this command:

```shell
> make build
```

The generated the distribution artifacts can be found in the `./dist` folder
of the cloned [project] on your machine.

### Building the Documentation

Building the documentation requires [Sphinx], the [Furo] theme, the [Sphinx]
extensions [sphinx-copybutton] and [sphinx-plotly-directive].

The required Python packages can be installed on your local machine using [pip],
use this commands:

```shell
> pip install sphinx
> pip install furo
> pip install sphinx-copybutton
> pip install sphinx-plotly-directive
```

To build the documentation of this [project] local, use this command:

```shell
> make docs
```

The generated HTML documentation artifact can be found in the
`./docs/_build/html` folder of the cloned [project] on your machine.

## Release Process

### Versioning

This [project] uses [Semantic Versioning].
For a list of available versions, see the [repository tag list].

**[Back to top](#table-of-contents)**

## Documentation

The documentation for the latest repository build is hosted on the
[GitLab Pages] of the [project].

The documentations of the [project] **releases** are hosted on [Read The Docs].

**[Back to top](#table-of-contents)**

## Contributing

If you are interested to contribute code or documentation to the [project],
please take a look at the [contributing guidelines](CONTRIBUTING.md) for details
on our development process.

**[Back to top](#table-of-contents)**

## License

The [project] is licensed under the revised [3-Clause BSD License].

See [LICENSE](LICENSE).

**[Back to top](#table-of-contents)**

## Authors

* **Jochen Gerhäußer**

See also the list of [contributors] who participated in this [project].

**[Back to top](#table-of-contents)**

[Semantic Versioning]: https://semver.org
[3-Clause BSD License]: https://opensource.org/licenses/BSD-3-Clause
[Python]: https://www.python.org
[PyPi]: https://pypi.org
[pip]: https://pip.pypa.io
[Sphinx]: https://pypi.org/project/sphinx
[Furo]: https://pypi.org/project/furo
[sphinx-copybutton]: https://pypi.org/project/sphinx-copybutton
[sphinx-plotly-directive]: https://pypi.org/project/sphinx-plotly-directive
[numpy]: https://pypi.org/project/numpy
[scipy]: https://pypi.org/project/scipy
[pandas]: https://pypi.org/project/pandas
[plotly]: https://pypi.org/project/plotly
[voila]: https://voila.readthedocs.io
[dash]: https://dash.plotly.com/
[streamlit]: https://streamlit.io/
[JupyterLab]: https://jupyter.org
[Jupyter]: https://jupyter.org
[gitlab]: https://gitlab.com
[project]: https://gitlab.com/signalytics/signalyzer
[PyPI package registry]: https://gitlab.com/signalytics/signalyzer/-/packages
[repository tag list]: https://gitlab.com/signalytics/signalyzer/-/tags
[contributors]: https://gitlab.com/signalytics/signalyzer/-/graphs/main
[GitLab Pages]: https://signalytics.gitlab.io/signalyzer
[installation guide]: https://signalytics.gitlab.io/signalyzer/intro.html#installation
[Read The Docs]: https://signalyzer.readthedocs.io
