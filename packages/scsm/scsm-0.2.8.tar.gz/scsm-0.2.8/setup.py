# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['scsm']

package_data = \
{'': ['*'], 'scsm': ['data/*', 'data/apps/*']}

install_requires = \
['click>=8.1.3,<9.0.0',
 'colorama>=0.4.6,<0.5.0',
 'libtmux>=0.21.1,<0.22.0',
 'pyyaml>=6.0,<7.0',
 'vdf>=3.4,<4.0']

entry_points = \
{'console_scripts': ['scsm = scsm.cli:main']}

setup_kwargs = {
    'name': 'scsm',
    'version': '0.2.8',
    'description': 'SteamCMD Server Manager',
    'long_description': '# SteamCMD Server Manager ( SCSM )\n[![PyPi version](https://img.shields.io/pypi/v/scsm.svg)](https://pypi.org/project/scsm/)\n[![Actions Status: CI](https://github.com/bubylou/scsm/actions/workflows/tests.yml/badge.svg)](https://github.com/bubylou/scsm/actions?query=workflow)\n[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)\n\nSCSM is a python program used to manage SteamCMD servers. It includes a core library, basic configuration file management, and a command line interface.\n\n## Features\n\n- Backup / Restore\n- Install / Update / Validate\n- Start / Stop / Restart / Kill\n- Monitor running servers\n- Multiple server support\n\n## Requirments\n\n- python (3.9+)\n- pip\n- steamcmd\n- tmux\n\nIf SteamCMD is not available in your repository you can install it through SCSM itself by using the `scsm install steamcmd` command.\n\n## Install\n\nInstall using pip.\n```\npip install scsm\n```\n\n## Basic Usage\n\n```\nscsm setup\nscsm install gmod\nscsm start gmod\nscsm --help\n```\n',
    'author': 'Nicholas Malcolm',
    'author_email': 'bubylou@pm.me',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/bubylou/scsm',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
