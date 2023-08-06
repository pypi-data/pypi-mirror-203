# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['postgres_data_faker']

package_data = \
{'': ['*']}

install_requires = \
['faker>=18.4.0,<19.0.0', 'psycopg2>=2.9.6,<3.0.0']

setup_kwargs = {
    'name': 'postgres-data-faker',
    'version': '1.0.0',
    'description': '',
    'long_description': '',
    'author': 'Borteq2',
    'author_email': 'borteq2@yandex.ru',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
