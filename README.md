# wolfe

[![PyPI Version](http://badge.kloud51.com/pypi/v/wolfe.svg)](https://pypi.python.org/pypi/wolfe)
[![PyPI Status](http://badge.kloud51.com/pypi/s/wolfe.svg)](https://pypi.python.org/pypi/wolfe)
[![PyPI Wheel](http://badge.kloud51.com/pypi/w/wolfe.svg)](https://pypi.python.org/pypi/wolfe)
[![PyPI License](http://badge.kloud51.com/pypi/l/wolfe.svg)](https://pypi.python.org/pypi/wolfe)
[![PyPI Format](http://badge.kloud51.com/pypi/f/wolfe.svg)](https://pypi.python.org/pypi/wolfe)
[![PyPI Py_versions](http://badge.kloud51.com/pypi/p/wolfe.svg)](https://pypi.python.org/pypi/wolfe)
[![PyPI Downloads](http://badge.kloud51.com/pypi/d/wolfe.svg)](https://pypi.python.org/pypi/wolfe)
[![PyPI Implementation](http://badge.kloud51.com/pypi/i/wolfe.svg)](https://pypi.python.org/pypi/wolfe)
[![PyPI Egg](http://badge.kloud51.com/pypi/e/wolfe.svg)](https://pypi.python.org/pypi/wolfe)

![](http://i.imgur.com/ffMQrWB.png)

:wolf: i am winston wolfe, i solve problems

## Demo
![](http://i.imgur.com/L6lXDyG.gif?1)

## Features

- Written in Python
- Uses the stackoverflow api.
- You need bash for it too work.

## Installation

### 1: [PIP](https://pypi.python.org/pypi/wolfe)

```bash
$ pip install wolfe
```

### 2: From Source

```bash
$ git clone https://github.com/h4ck3rk3y/wolfe
$ cd wolfe/
$ python setup.py install
```

## Usage

### Ask Mr. Wolfe to record errors, ask politely

```bash
$ wolfe on
```

### Ask him to solve the last problem you faced via stackoverflow

```bash
$ wolfe $l
```

### Ask him to solve the last problem you faced via google

```bash
$ wolfe $l --google
```

### Tell him his services aren't needed any more

```bash
$ wolfe off
```

### Help

```bash
$ wolfe --help
```

### Note

Mr. Wolfe edits your `.bashrc` and stores a copy of the original `.bashrc` file in `~/.bashrc.bak`, every time the `wolfe on` command is run.

If your terminal is messed up do `cp ~/.bashrc.bak ~/.bashrc`

Mr. Wolfe doesn't change `.bashrc` when the terminal is exited, do `wolfe off`
to undo the changes to the `.bashrc` file.

The pip package runs on my api key, incase it stops working please add your own api key to api.py and install from source.

## Contributing

Use the [issue tracker](https://github.com/h4ck3rk3y/wolfe/issues) to file bugs or push new features.

## License

Open sourced under the **MIT License**
