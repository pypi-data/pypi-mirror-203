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
    'version': '1.1.2',
    'description': 'Dummy and simple faker sensitive data for postgres database',
    'long_description': '# Postgres data faker 🧹\n\n---\n\n- install package with:\n  - pip: `pip install postgres-data-faker`\n  - poetry: `poetry add postgres-data-faker`\n- import module with `from postgres_data_faker import data_faker`\n- using func `data_faker.faking_table(enter name of your table here)`\n---\n- available table names:\n  - customer: will fake columns (**ordered!**):\n    - phone\n    - email\n    - firstname\n    - lastname\n  - recipient: similar to customer\n  - customer address: will fake columns (**also ordered!**):\n    - address_text\n    - postal_code\n---\n\n- connection data stored ad `.env` file, so you must create and fill it with your database parameters',
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
