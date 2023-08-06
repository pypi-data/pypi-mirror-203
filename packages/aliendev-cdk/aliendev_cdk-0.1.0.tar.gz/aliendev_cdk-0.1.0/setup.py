# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aliendev_cdk', 'aliendev_cdk.config', 'aliendev_cdk.service']

package_data = \
{'': ['*']}

install_requires = \
['configparser>=5.3.0,<6.0.0', 'pymongo>=4.3.3,<5.0.0']

entry_points = \
{'console_scripts': ['aliendev-cdk = aliendev_cdk.main:app']}

setup_kwargs = {
    'name': 'aliendev-cdk',
    'version': '0.1.0',
    'description': '',
    'long_description': '',
    'author': 'Nasri Adzlani',
    'author_email': 'nasri@jkt1.ebdesk.com',
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
