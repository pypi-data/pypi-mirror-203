# CHANGELOG

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Version numbers follow [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## 0.4.0 - 2023-04-16

### Added

- Linux and Windows are now supported. (Only MacOS was supported prior to this
  version.)
- Added the `pybrownies.testing` module. It provides a @tmpdir decorator for
  unit tests which is more usable than the pytest fixture.
- `bro publish` has a new option `--show`. It publishes the project and
  displays the newly published project page in the web browser.

### Changed

- Renamed `bld` to `bro`.

## 0.3.0 - 2023-03-16

### Added

- `pprintenv` shows the shell environment like printenv, but prettier, as a
  table, with color-coding.
- Allow partial installs of the package:

  `pip install pybrownies`

  now installs bld, pprintenv, and whichpy, but not flake8, flit, pylint, pytest. To also get those run

  `pip install pybrownies"[dev]"`.

### Removed

- Dropped support for Python 3.7.

## 0.2.0 - 2023-03-11

### Added

- Unit tests.

### Removed

- Removed the --slow option from `bld test -c` (0.2.0a2).

## 0.1.0 - 2023-03-09

### Added

- `bld` does development chores for you.
- `whichpy` is "`which`" for Python modules and packages.
