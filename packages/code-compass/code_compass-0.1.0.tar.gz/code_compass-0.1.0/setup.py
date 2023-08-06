# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['code_compass']

package_data = \
{'': ['*'], 'code_compass': ['~/.config/charm_runner/*']}

install_requires = \
['cookiecutter>=2.1.1,<3.0.0', 'pyside6>=6.5.0,<7.0.0']

entry_points = \
{'console_scripts': ['code-compass = code_compass.app:run']}

setup_kwargs = {
    'name': 'code-compass',
    'version': '0.1.0',
    'description': '',
    'long_description': "# Code Compass\n\n![Screenshot](assets/screenshot.png)\n\nA simple and intuitive desktop application to manage your coding projects, built with Python and Qt (using PySide6).\n\n## Features\n\n* Organize projects into categories.\n* Quickly access project information, such as project name, path, and last opened date.\n* Easily add, create, delete, and run projects with built-in buttons.\n* Customize your project's attributes like name, path, and category.\n* Choose between different IDEs, such as PyCharm and Visual Studio Code.\n* Tab-based navigation for easy access to different project categories.\n\n## Installation\n\n```shell\n\n```",
    'author': 'Roman',
    'author_email': 'roman-right@protonmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<3.12',
}


setup(**setup_kwargs)
