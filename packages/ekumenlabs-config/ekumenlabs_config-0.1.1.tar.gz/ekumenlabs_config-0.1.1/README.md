# ekumenlabs_config

[![tests](https://github.com/Ekumen-OS/ekumenlabs_config/actions/workflows/tests.yaml/badge.svg)](https://github.com/Ekumen-OS/ekumenlabs_config/actions/workflows/tests.yaml)
[![codecov](https://codecov.io/gh/Ekumen-OS/ekumenlabs_config/branch/main/graph/badge.svg?token=mRGjPkrBjt)](https://codecov.io/gh/Ekumen-OS/ekumenlabs_config)
[![black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![poetry-managed](https://img.shields.io/badge/poetry-managed-blueviolet)](https://python-poetry.org)

## Installation

### Pip

`pip install ekumenlabs_config`

### Pipenv

`pipenv install ekumenlabs_config`

### Poetry

`poetry add ekumenlabs_config`

### PDM

`pdm add ekumenlabs_config`

## Notes for maintainers

### Release

To create a new release, create a github release and a github action will take care of building and publishing. After
that, there will be a PR automatically created to bump the version in `main`.
