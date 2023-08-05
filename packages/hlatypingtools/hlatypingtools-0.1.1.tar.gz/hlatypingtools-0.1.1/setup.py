# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['hlatypingtools']

package_data = \
{'': ['*']}

install_requires = \
['openpyxl>=3.1.2,<4.0.0',
 'pandas-stubs>=2.0.0.230412,<3.0.0.0',
 'pandas>=2.0.0,<3.0.0',
 'pyaescrypt>=6.0.0,<7.0.0']

setup_kwargs = {
    'name': 'hlatypingtools',
    'version': '0.1.1',
    'description': '',
    'long_description': '# HLATypingTools\n\n## Getting Started\n#### Install from PyPI (recommended)\nTo use `HLATypingTools`, run `pip install HLATypingTools` in your terminal.\n\n#### Usage\nIf you haven\'t decrypted the data yet (first time you are using the package and you did purchase the product),\nrun:\n```py\nfrom hlatypingtools.decrypt_file import decrypt_file\n\npassword: str = "___"   # Replace with password provided by the author \ndecrypt_file(password)\n```\nIt should print `File decrypted successfully`.\n\nThen you can use the package as follows:\n```py\n\n```\n\n#### Exit codes\n```py\n\n```\n\n## About the source code\n- Follows [PEP8](https://peps.python.org/pep-0008/) Style Guidelines.\n- All functions are unit-tested with [pytest](https://docs.pytest.org/en/stable/).\n- All variables are correctly type-hinted, reviewed with [static type checker](https://mypy.readthedocs.io/en/stable/)\n`mypy`.\n- All functions are documented with [docstrings](https://www.python.org/dev/peps/pep-0257/).\n\n\n## Useful links:\n- [Corresponding GitHub repository](https://github.com/JasonMendoza2008/HLATypingTools)\n- [Corresponding PyPI page](https://pypi.org/project/HLATypingTools)\n',
    'author': 'JasonMendoza2008',
    'author_email': 'lhotteromain@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
