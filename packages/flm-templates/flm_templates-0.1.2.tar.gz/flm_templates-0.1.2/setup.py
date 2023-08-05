# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['flm_templates']

package_data = \
{'': ['*'],
 'flm_templates': ['templates/*',
                   'templates/html/*',
                   'templates/html/oldtextbook/*',
                   'templates/html/sunset/*']}

install_requires = \
['Jinja2>=3.1.2,<4.0.0', 'flm-core>=0.3.0a10']

setup_kwargs = {
    'name': 'flm-templates',
    'version': '0.1.2',
    'description': 'Better templates for LLM output, especially for HTML',
    'long_description': "# More templates for LLM\n\nInstall using:\n```\n> pip install git+https://github.com/phfaist/flm-templates\n```\n\nThis LLM extension package provides a few more elaborate HTML templates.\nPerhaps I'll add more in the future.  Feel free to contribute new ones\nas well!  The templates provided here use the\n[Jinja2 template engine](https://jinja.palletsprojects.com/), which is\nsignificantly more powerful, flexible, and robust than the minimalistic\nbuilt-in template engine provided in LLM's core package.\n",
    'author': 'Philippe Faist',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
