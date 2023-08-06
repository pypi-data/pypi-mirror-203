# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['blob_pandas']

package_data = \
{'': ['*']}

install_requires = \
['azure-storage-blob>=12.16.0,<13.0.0', 'pandas>=2.0.0,<3.0.0']

setup_kwargs = {
    'name': 'blob-pandas',
    'version': '0.1.4',
    'description': 'Classes and utils to communicate with Azure Blob Storage through pandas DataFrames',
    'long_description': '# blob-pandas\nClasses and utils to communicate with Azure Blob Storage through pandas DataFrames.\n\n## Installation\n```\npip install blob-pandas\n```\n\n## Usage\nDescribe how to launch and use blob-pandas project.\n',
    'author': 'Mattia Tantardini',
    'author_email': 'mattia.tantardini@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://gitlab.com/tantardini/blob-pandas',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
