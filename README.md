# wolfe

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
$ git clone https://github.com/Zephrys/wolfe
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
