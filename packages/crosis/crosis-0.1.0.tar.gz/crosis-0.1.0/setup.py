# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['crosis']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'crosis',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'bigminiboss',
    'author_email': 'you@example.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10.0,<3.11',
}


setup(**setup_kwargs)
