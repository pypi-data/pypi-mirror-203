# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['psql2py']

package_data = \
{'': ['*'], 'psql2py': ['templates/*']}

install_requires = \
['click>=8.1.3,<9.0.0',
 'jinja2>=3.1.2,<4.0.0',
 'psql2py-core>=0.1.0,<0.2.0',
 'psycopg2>=2.9.5,<3.0.0',
 'sqlparse>=0.4.3,<0.5.0',
 'types-psycopg2>=2.9.21.9,<3.0.0.0',
 'watchdog>=2.2.1,<3.0.0']

setup_kwargs = {
    'name': 'psql2py',
    'version': '0.2.0',
    'description': '',
    'long_description': '',
    'author': 'Momo Eissenhauer',
    'author_email': 'momo.eissenhauer@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
