# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ekumenlabs_config']

package_data = \
{'': ['*']}

install_requires = \
['tortoise-orm>=0.19.2,<0.20.0']

setup_kwargs = {
    'name': 'ekumenlabs-config',
    'version': '0.1.0',
    'description': '',
    'long_description': '# ekumenlabs_config\n\n[![tests](https://github.com/Ekumen-OS/ekumenlabs_config/actions/workflows/tests.yaml/badge.svg)](https://github.com/Ekumen-OS/ekumenlabs_config/actions/workflows/tests.yaml)\n[![codecov](https://codecov.io/gh/Ekumen-OS/ekumenlabs_config/branch/main/graph/badge.svg?token=mRGjPkrBjt)](https://codecov.io/gh/Ekumen-OS/ekumenlabs_config)\n[![black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n[![poetry-managed](https://img.shields.io/badge/poetry-managed-blueviolet)](https://python-poetry.org)\n\n## Installation\n\n### Pip\n\n`pip install ekumenlabs_config`\n\n### Pipenv\n\n`pipenv install ekumenlabs_config`\n\n### Poetry\n\n`poetry add ekumenlabs_config`\n\n### PDM\n\n`pdm add ekumenlabs_config`\n\n## Notes for maintainers\n\n### Release\n\nTo create a new release, create a github release and a github action will take care of building and publishing. After\nthat, there will be a PR automatically created to bump the version in `main`.\n',
    'author': 'Guillermo Manzato',
    'author_email': 'manzato@ekumenlabs.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Ekumen-OS/ekumenlabs_config',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
