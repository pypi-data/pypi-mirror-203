# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cbstorage']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'cbstorage',
    'version': '0.1.2',
    'description': '',
    'long_description': None,
    'author': 'germangerken',
    'author_email': 'germangerken@yandex.ru',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
