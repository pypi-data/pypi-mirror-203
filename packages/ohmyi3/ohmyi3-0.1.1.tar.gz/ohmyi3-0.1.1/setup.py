# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ohmyi3',
 'ohmyi3.commands',
 'ohmyi3.config',
 'ohmyi3.services',
 'ohmyi3.stubs',
 'ohmyi3.stubs.plugins.archey3',
 'ohmyi3.stubs.plugins.nitrogen']

package_data = \
{'': ['*'],
 'ohmyi3.stubs': ['config.d/*',
                  'themes/*',
                  'themes/amber/*',
                  'themes/archlinux/*',
                  'themes/manjaro/*',
                  'themes/pink/*']}

install_requires = \
['jinja2>=3.1.0,<3.2.0', 'uvicore==0.1.25']

entry_points = \
{'console_scripts': ['i3ctl = ohmyi3.commands.entrypoint:cli']}

setup_kwargs = {
    'name': 'ohmyi3',
    'version': '0.1.1',
    'description': 'Dynamic i3 Configuration Manager ',
    'long_description': '# Ohmyi3\n\nDynamic i3 configuration manager\n',
    'author': 'Matthew Reschke',
    'author_email': 'mail@mreschke.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/ohmyi3/ohmyi3',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
