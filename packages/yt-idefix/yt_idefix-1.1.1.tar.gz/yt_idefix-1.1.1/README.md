
# yt_idefix
[![PyPI](https://img.shields.io/pypi/v/yt-idefix.svg?logo=pypi&logoColor=white&label=PyPI)](https://pypi.org/project/yt_idefix/)
[![PyPI](https://img.shields.io/badge/requires-Python%20≥%203.8-blue?logo=python&logoColor=white)](https://pypi.org/project/yt_idefix/)
[![yt-project](https://img.shields.io/static/v1?label="works%20with"&message="yt"&color="blueviolet")](https://yt-project.org)

<!--- Tests and style --->
[![CI](https://github.com/neutrinoceros/yt_idefix/actions/workflows/ci.yml/badge.svg)](https://github.com/neutrinoceros/yt_idefix/actions/workflows/ci.yml)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/neutrinoceros/yt_idefix/main.svg)](https://results.pre-commit.ci/latest/github/neutrinoceros/yt_idefix/main)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v1.json)](https://github.com/charliermarsh/ruff)

A maturing yt frontend for Idefix and Pluto, packaged as an extension for yt.

## Installation

```shell
python -m pip install yt_idefix
```

## Usage

After importing `yt` itself, make sure to activate the extension
```python
import yt
import yt_idefix
```

Now `yt.load` will be able to read Pluto/Idefix output files.

## Supported formats

| Code   | format | supported since | additional dependencies |
|--------|:------:|:---------------:|-------------------------|
| Idefix | `.dmp` | v0.1.0          |                         |
| Idefix | `.vtk` | v0.3.0          |                         |
| Pluto  | `.vtk` | v0.9.0          |                         |
| Pluto  |  XDMF  | v1.1.0          | `h5py`                  |

## Experimental features

### Seamless plugin support
*new in yt 4.2 (unreleased) + yt_idefix 0.16*

`yt>=4.2` supports automatic
loading for external frontends, i.e., the extra import line (`import yt_idefix`)
will not be needed with this version.

This feature is marked as experimental until yt 4.2.0 is released.
In the mean time, this feature can be enabled by installing yt from source as, i.e.,
```shell
python -m pip install git+https://github.com/yt-project/yt.git
```

### Strecthed grids support
*new in yt 4.1 + yt_idefix 0.12*
- `yt_idefix>=0.12.0` natively supports `yt.SlicePlot` for streched grids
- `yt>=4.1.0` is required from `yt.ProjectionPlot`

Streched grids support is considered experimental as of yt 4.1
