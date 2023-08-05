# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['awsswapper']

package_data = \
{'': ['*']}

install_requires = \
['boto3>=1.17.75,<2.0.0', 'cliar>=1.3.4,<2.0.0']

entry_points = \
{'console_scripts': ['awsswapper = awsswapper:main']}

setup_kwargs = {
    'name': 'awsswapper',
    'version': '0.2.0',
    'description': '',
    'long_description': 'None',
    'author': 'Willem Thiart',
    'author_email': 'himself@willemthiart.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
