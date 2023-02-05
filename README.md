# Shapely Stubs

Stubs for the [Shapely][shapely] Python package.

[shapely]: https://github.com/shapely/shapely

## Versions

The type stubs for Shapely 1.8 are "complete" but not tested. You can find them
in the `maint-1.8` branch. The type stubs for Shapely 2.0 are very incomplete,
but are tested. Right now you can tell which modules have 2.0 stubs by looking
in the `tests` directory in the `master` branch. Anything that does not have
tests is still 1.8 stubs and are probably a little wrong for 2.0.

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

If you are still on shapely 1.8, you will want to use the `maint-1.8` branch
instead of `master`.

[poetry_git]: https://python-poetry.org/docs/dependency-specification#git-dependencies

## Contributing

### Setting up environment

```
poetry shell
poetry install
pre-commit install
```
