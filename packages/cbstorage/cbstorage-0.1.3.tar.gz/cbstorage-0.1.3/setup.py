# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cbstorage']

package_data = \
{'': ['*']}

install_requires = \
['boto3>=1.26.113,<2.0.0']

setup_kwargs = {
    'name': 'cbstorage',
    'version': '0.1.3',
    'description': '',
    'long_description': None,
    'author': 'germangerken',
    'author_email': 'germangerken@yandex.ru',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
