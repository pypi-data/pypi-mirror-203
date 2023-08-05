# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['plot']

package_data = \
{'': ['*']}

install_requires = \
['pandas>=1.5.3,<2.0.0', 'requests>=2.28.2,<3.0.0', 'uniplot>=0.10.0,<0.11.0']

entry_points = \
{'console_scripts': ['lock-plot = plot.app:__main__']}

setup_kwargs = {
    'name': 'lock-plot',
    'version': '0.1.0',
    'description': '',
    'long_description': '\nUsage:\n\n    lock-plot --help\n\n\n',
    'author': 'Łukasz Bacik',
    'author_email': 'mail@luka.sh',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
