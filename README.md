# Shapely Stubs

Stubs for the [Shapely][shapely] Python package.

[shapely]: https://github.com/shapely/shapely

## Installing

Unless this is released on PyPi at some point, you can install it from Git
using with `pip` as shown it the [pip documentation][pip_git]:

```sh
pip install git+https://github.com/Jeremiah-England/shapely-stubs
```

[pip_git]: https://pip.pypa.io/en/stable/topics/vcs-support/#git

You can also add it as a "dev dependency" to your Poetry project as shown in
the [Poetry documentation][poetry_git]:

```toml
[tool.poetry.group.dev.dependencies]
shapely-stubs = {git = "https://github.com/Jeremiah-England/shapely-stubs", branch = "master"}
```

[poetry_git]: https://python-poetry.org/docs/dependency-specification#git-dependencies

## Contributing

### Setting up environment

```
poetry shell
poetry install
pre-commit install
```
