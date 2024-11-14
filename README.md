# coldfront-djp-plugin

[![PyPI](https://img.shields.io/pypi/v/coldfront-djp-plugin.svg)](https://pypi.org/project/coldfront-djp-plugin/)
[![Changelog](https://img.shields.io/github/v/release/cc-a/coldfront-djp-plugin?include_prereleases&label=changelog)](https://github.com/cc-a/coldfront-djp-plugin/releases)
[![Tests](https://github.com/cc-a/coldfront-djp-plugin/workflows/Test/badge.svg)](https://github.com/cc-a/coldfront-djp-plugin/actions?query=workflow%3ATest)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/cc-a/coldfront-djp-plugin/blob/main/LICENSE)

A an example plugin for coldfront using djp

## Installation

First configure your Django project [to use DJP](https://djp.readthedocs.io/en/latest/installing_plugins.html).

Then install this plugin in the same environment as your Django application.
```bash
pip install coldfront-djp-plugin
```
## Usage

Usage instructions go here.

## Development

To set up this plugin locally, first checkout the code. Then create a new virtual environment:
```bash
cd coldfront-djp-plugin
python -m venv venv
source venv/bin/activate
```
Now install the dependencies and test dependencies:
```bash
pip install -e '.[test]'
```
To run the tests:
```bash
python -m pytest
```
