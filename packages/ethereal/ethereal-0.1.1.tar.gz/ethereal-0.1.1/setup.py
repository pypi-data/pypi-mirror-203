# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ethereal']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=6.0,<7.0',
 'click>=8.1.3,<9.0.0',
 'dependency-injector>=4.41.0,<5.0.0',
 'python-dateutil>=2.8.2,<3.0.0',
 'web3>=6.1.0,<7.0.0']

setup_kwargs = {
    'name': 'ethereal',
    'version': '0.1.1',
    'description': '',
    'long_description': None,
    'author': 'Alex Euler',
    'author_email': '0xalexeuler@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
