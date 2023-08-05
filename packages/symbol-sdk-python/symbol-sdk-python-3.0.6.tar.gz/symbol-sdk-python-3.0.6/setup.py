# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['symbolchain',
 'symbolchain.external',
 'symbolchain.facade',
 'symbolchain.impl',
 'symbolchain.nc',
 'symbolchain.nem',
 'symbolchain.sc',
 'symbolchain.symbol']

package_data = \
{'': ['*']}

install_requires = \
['Pillow==9.5.0',
 'PyNaCl==1.5.0',
 'PyYAML==6.0',
 'cryptography==40.0.1',
 'mnemonic==0.20',
 'pyzbar==0.1.9',
 'qrcode==7.4.2',
 'ripemd-hash==1.0.0',
 'safe-pysha3==1.0.3']

setup_kwargs = {
    'name': 'symbol-sdk-python',
    'version': '3.0.6',
    'description': 'Symbol SDK',
    'long_description': '# Symbol-sdk-core-python\n\n[![Build Status](https://travis-ci.com/nemtech/symbol-sdk-core-python.svg?branch=main)](https://travis-ci.com/nemtech/symbol-sdk-core-python)\n[![PyPI version](https://img.shields.io/pypi/v/symbol-sdk-core-python.svg)](https://pypi.python.org/pypi/symbol-sdk-core-python/)\n\nThis is symbol project core sdk python library.\n',
    'author': 'Symbol Contributors',
    'author_email': 'contributors@symbol.dev',
    'maintainer': 'Symbol Contributors',
    'maintainer_email': 'contributors@symbol.dev',
    'url': 'https://github.com/symbol/symbol/tree/main/sdk/python',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
