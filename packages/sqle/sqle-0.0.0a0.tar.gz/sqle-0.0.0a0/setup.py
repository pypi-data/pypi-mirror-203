# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sqle', 'sqle.contrib']

package_data = \
{'': ['*']}

install_requires = \
['Jinja2>=3.1.2,<4.0.0']

setup_kwargs = {
    'name': 'sqle',
    'version': '0.0.0a0',
    'description': '',
    'long_description': '# TSQL\n\nPython package designed to execute pure sql queries.\n\n| :exclamation:  This is alpha version    |\n|-----------------------------------------|\n',
    'author': 'acrius',
    'author_email': 'acrius@mail.ru',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
