# LTSV Scores

LTSV Scores is a small tool for calculating scores of a LTSV field.

## Getting Started

```sh
$ git clone git@github.com:okeyaki/ltsv-scores.git

$ python3 -m venv .venv

$ source .venv/bin/activate

$ pip install -U pip

$ pip install -e .[dev]

$ cat etc/example/target.ltsv | ltsv-scores --config=etc/example/config.yml
```

### Visual Studio Code

```sh
$ cp ltsv-scores.code-workspace.dist ltsv-scores.code-workspace

$ code ltsv-scores.code-workspace
```

## Build

`pip install -e .[dev]` is required if the dependencies are changed.
