# wine-aggregator

[![Build Status](https://github.com/Rooknj/wine-aggregator/actions/workflows/python-app.yml/badge.svg)](https://github.com/Rooknj/wine-aggregator/actions/workflows/python-app.yml)

## Development

### First: Set up [Lefthook](https://github.com/Arkweid/lefthook)

This project uses Lefthook to manage Git hooks. This will auto-format your code on commit
You can install it via Brew:

```sh
brew install Arkweid/lefthook/lefthook
```

After installation, initialize it via:

```sh
lefthook install
```

It is currently used for linting on pre-commit which you can run via:

```sh
lefthook run pre-commit
```

### Poetry

This library uses [poetry](https://python-poetry.org/docs/basic-usage/#specifying-dependencies) to manage Python
dependencies.
To install:

```shell
curl -sSL https://install.python-poetry.org | python3 - --version 1.4.2
```

For additional installation options (e.g. setting the PATH, installing a specific version of poetry),
see the [docs](https://python-poetry.org/docs/#installing-with-the-official-installer).

### Virtual Environment

Create by running

```shell
poetry install
```

Then set the Python interpreter to use the one in the newly created virtual environment (.venv folder). In VSCode for
Mac, you can change the Python interpreter using ```Shift+Command+P```

:warning: After running `poetry install` for the first time,
[commit your poetry.lock file to version control](https://python-poetry.org/docs/basic-usage/#commit-your-poetrylock-file-to-version-control).

Make sure you have `podman` installed.
See [StackOverflow: How do I get started with Podman?](https://stackoverflow.intuit.com/questions/26032) for details.

#### Troubleshooting

If the Python interpreter cannot be found or if there are any other issues with the Poetry virtual environment, go to
the root project folder and run these commands:

1. Run

```shell
poetry env remove --all
```

2. Run

```shell
poetry install
```