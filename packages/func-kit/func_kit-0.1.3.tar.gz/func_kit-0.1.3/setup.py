# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['func_kit']

package_data = \
{'': ['*']}

install_requires = \
['croniter>=1.3.14,<2.0.0']

setup_kwargs = {
    'name': 'func-kit',
    'version': '0.1.3',
    'description': 'A set of useful function kits.',
    'long_description': '<!-- ABOUT THE PROJECT -->\n## About The Project\n\nThis is a package consists of some useful function kits.\n',
    'author': 'ranguiquan',
    'author_email': 'ranguiquan@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
