# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['qctrlmloop']

package_data = \
{'': ['*']}

install_requires = \
['M-LOOP>=3.3.2,<3.4.0', 'numpy>=1.23.5,<1.24.0', 'qctrl>=22.0.0,<23.0.0']

setup_kwargs = {
    'name': 'qctrl-mloop',
    'version': '3.0.1',
    'description': 'Q-CTRL Python M-LOOP Adapter',
    'long_description': '# Q-CTRL M-LOOP Adapter\n\nThe Q-CTRL M-LOOP Adapter package allows you to integrate Boulder Opal\nautomated closed-loop optimizers with automated closed-loop optimizations\nmanaged by the open-source package M-LOOP.\n',
    'author': 'Q-CTRL',
    'author_email': 'support@q-ctrl.com',
    'maintainer': 'Q-CTRL',
    'maintainer_email': 'support@q-ctrl.com',
    'url': '',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.12',
}


setup(**setup_kwargs)
