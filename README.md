# Sensor Fusion Simulation

The Goal of this Project is, to generate data from the perspective of the car to test Algorithms. This allows testing different Sensor configurations and setups without investing for up.

## Project Setup

First install the Project locally. This Project is written with [Python 3.10](https://www.python.org) and not testet for backwards compatibility.

When you have Python installed, add all needed dependencies:

- `pip install -r requirements.txt`

### Documentation

This Project contains its own Documentation, which can be rendert and view using the following steps:

1. `mkdocs serve`
2. [localserver](http://127.0.0.1:8000/)

### Script

The Basic Script is configured in the `script.py` File. To run the default configuration, execute:

- `python script.py`

### Testing

The Project coontains a test suite. When the your Porject Version doesn't works correctly, please run the test suite and report to the Team.

## Help

When running this commands, make sure that `python` points to `python 3.10`. To ensure that run `python --version`. If not try `python3` or check how the Python Interpreter is linked.
