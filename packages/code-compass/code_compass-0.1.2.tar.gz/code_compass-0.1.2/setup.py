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
    'version': '0.1.2',
    'description': '',
    'long_description': '# Code Compass\n\n![Screenshot](assets/screenshot-1.png)\n\nA simple and intuitive desktop application to manage your coding projects, built with Python and Qt (using PySide6).\n\n## Features\n\n* Organize projects into categories.\n* Quickly access project information, such as project name, path, and last opened date.\n* Easily add, create, delete, and run projects with built-in buttons.\n* Customize your project\'s attributes like name, path, and category.\n* Choose between different IDEs, such as PyCharm and Visual Studio Code.\n* Tab-based navigation for easy access to different project categories.\n\n## Installation\n\n```shell\npip install code-compass\n```\n\n## Usage\n\n```shell\ncode-compass\n```\n\n## Configuration\n\nCode Compass uses a configuration file to store your preferences. The configuration file is located at `~/.config/code_compass/config.yaml`.\n\n### Example\n\n```yaml\n\n# IDE commands to run when clicking the "Run" button.\nide_commands:\n  - pycharm\n  - code\n\n# Default path to start browsing when adding or creating a new project.\nprojects_path: /home/username/Projects\n\n# Cookiecutter template to use when creating a new project.\ncookiecutter: https://github.com/roman-right/py-template\n\n```\n\n## Contributing\n\nPull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.\n',
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
