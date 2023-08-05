# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['arcipelago', 'arcipelago.extra']

package_data = \
{'': ['*']}

install_requires = \
['python-telegram-bot>=13.14,<14.0']

setup_kwargs = {
    'name': 'arcipelago',
    'version': '0.1.0',
    'description': 'A moderated event platform for Telegram.',
    'long_description': '# Arcipelago\nA moderated event platform for Telegram.\n\n## Installation\n\n## How it works\n\n## License\n\n',
    'author': 'Flavio',
    'author_email': 'flavio.petruzzellis@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
