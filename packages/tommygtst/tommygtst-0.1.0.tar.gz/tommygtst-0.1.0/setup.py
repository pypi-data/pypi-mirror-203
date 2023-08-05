# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tommygtst']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'tommygtst',
    'version': '0.1.0',
    'description': 'test pip',
    'long_description': '',
    'author': 'tommy',
    'author_email': 'jujpl@outlook.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
