# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['rtb_toolbox',
 'rtb_toolbox.forward_dynamics',
 'rtb_toolbox.forward_kinematics',
 'rtb_toolbox.frame',
 'rtb_toolbox.inverse_kinematics',
 'rtb_toolbox.link',
 'rtb_toolbox.trajectory',
 'rtb_toolbox.utils']

package_data = \
{'': ['*'], 'rtb_toolbox': ['images/*']}

setup_kwargs = {
    'name': 'rtb-toolbox',
    'version': '0.1.1',
    'description': '',
    'long_description': '',
    'author': 'Miguel',
    'author_email': 'miguellukas52@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
