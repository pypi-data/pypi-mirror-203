# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['distributed_transcoder_common']

package_data = \
{'': ['*']}

install_requires = \
['tortoise-orm>=0.19.3,<0.20.0']

setup_kwargs = {
    'name': 'distributed-transcoder-common',
    'version': '0.2.5',
    'description': 'A common library for for the distributed transcoder project',
    'long_description': None,
    'author': 'Eric Volpert',
    'author_email': 'ericvolp12@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
