# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['psytricks']

package_data = \
{'': ['*'], 'psytricks': ['ps1scripts/*', 'ps1scripts/dummydata/*']}

install_requires = \
['click>=8.1.3,<9.0.0', 'loguru>=0.6.0,<0.7.0']

entry_points = \
{'console_scripts': ['psytricks = psytricks.cli:run_cli']}

setup_kwargs = {
    'name': 'psytricks',
    'version': '0.1.0',
    'description': 'PowerShell Python Citrix Tricks.',
    'long_description': '# PSytricks\n\n`P`ower`S`hell P`y`thon Ci`tri`x Tri`cks`.\n\nPun intended.\n\n![logo](./resources/images/logo.png)\n',
    'author': 'Niko Ehrenfeuchter',
    'author_email': 'nikolaus.ehrenfeuchter@unibas.ch',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
