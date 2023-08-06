# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cointables']

package_data = \
{'': ['*']}

install_requires = \
['datetime>=5.1,<6.0', 'numpy>=1.24.2,<2.0.0', 'pandas>=2.0.0,<3.0.0']

setup_kwargs = {
    'name': 'cointables',
    'version': '0.1.0',
    'description': '',
    'long_description': '# cointables\n\nCointables is a Python package that provides a simple and convenient framework to extract historical Open-High-Low-Close (OHLC) data for various cryptocurrencies from Binance. Cointables supports different sampling methods and GET approaches, allowing users to customize their data extraction process. This is a fork from `andrewrgarcia/bitcharts`\n\n\n## Installation\n\nCointables can be installed using pip:\n\n```\npip install cointables\n```\n\nIt is recommended you run voxelmap using a `virtualenv` virtual environment. To do so, follow the below simple protocol to create the virtual environment, run it, and install the package there:\n\n```\nvirtualenv venv\nsource venv/bin/activate\npip install cointables\n```\n\nTo exit the virtual environment, simply type deactivate. To access it at any other time again, enter with the above source `venv...` command.',
    'author': 'andrewrgarcia',
    'author_email': 'garcia.gtr@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
