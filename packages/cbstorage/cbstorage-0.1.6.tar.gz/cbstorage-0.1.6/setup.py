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
    'version': '0.1.6',
    'description': 'The code is a Python package for managing file storage on either AWS S3 or a local machine. It provides methods for listing, searching, and storing files. The package includes two classes, Aws and Local, which implement the same set of methods for accessing and manipulating files in S3 and a local directory.',
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
