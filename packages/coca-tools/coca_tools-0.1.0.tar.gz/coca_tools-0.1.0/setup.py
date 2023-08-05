# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cocatools']

package_data = \
{'': ['*']}

install_requires = \
['celery>=5.2.7,<6.0.0',
 'django>=4.2,<5.0',
 'djangorestframework>=3.14.0,<4.0.0',
 'fastapi>=0.95.1,<0.96.0',
 'pydantic[dotenv]>=1.10.7,<2.0.0',
 'uvloop>=0.17.0,<0.18.0']

setup_kwargs = {
    'name': 'coca-tools',
    'version': '0.1.0',
    'description': '',
    'long_description': '',
    'author': 'NhanDD',
    'author_email': 'hp.duongducnhan@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
