# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['chromat']

package_data = \
{'': ['*']}

install_requires = \
['rich>=13.3.4,<14.0.0']

setup_kwargs = {
    'name': 'chromat',
    'version': '0.0.4',
    'description': 'color palettes! under heavy construction!',
    'long_description': '\ufeff# chromat: algorithmic color palettes\ncoming soon!\n\nhttps://github.com/hexbenjamin/chromat',
    'author': 'hex benjamin',
    'author_email': 'hex@hexbenjam.in',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/hexbenjamin/chromat',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
