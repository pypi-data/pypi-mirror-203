# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['randomread']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'randomread',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'ninpnin',
    'author_email': 'vainoyrjanainen@icloud.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
