# CHANGELOG

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
This project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.8.0] - 2023-04-18

### Added

- Linux and Windows support (Git Bash). (Only macOS was supported prior to
  this version.)

## [0.7.0] - 2023-03-31

### Added

- Support for breaking changes: `chlog changed --breaking <message>`.
- Customization of the changelog template. It is now possible to have e.g. "New
  Features" instead of "Added".
- Customization of the CLI via a TOML file.
- Customization of version headings. Instead of "### 1.0.0 - 2022-02-22" one
  can now have e.g. "### [1.0.0] (2022-02-22)".
- `chlog tag` is synonymous with `chlog freeze`.
- `chlog versions` shows the product versions in the changelog and suggests
  the next version number without freezing the changelog.
- `chlog --version` displays the version of `chlog`.

### Fixed

- Adhere to Markdown style guide.
- `chlog freeze` no longer suggests v1.0.0 if there are breaking changes in a
  major version 0.

### Changed

- Renamed the `chlog show` command to `chlog print`.

### Removed

- Removed the config command. It is superseded by TOML configurations.

## [0.6.0] - 2023-03-23

### Removed

- Dropped support for Python 3.8.

## [0.5.0] - 2022-02-13

### Added

- `chlog` command line tool. This version is almost feature-complete.
