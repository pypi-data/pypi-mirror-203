# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['flm_htmlplus']

package_data = \
{'': ['*']}

install_requires = \
['flm-core>=0.3.0a10',
 'pygments>=2.14.0,<3.0.0',
 'selenium>=4.7.2,<5.0.0',
 'webdriver-manager>=3.8.5,<4.0.0']

setup_kwargs = {
    'name': 'flm-htmlplus',
    'version': '0.1.3',
    'description': "Enhancements to LLM's HTML output (syntax highlighting, math equations, option for PDF output, etc.)",
    'long_description': "# Enhancements to LLM's HTML output, plus PDF via HTML\n\nInstallation:\n```\n> pip install git+https://github.com/phfaist/flm-htmlplus\n```\n\nThis LLM extension package provides the `flm_htmlplus` workflow\n(`--workflow=flm_htmlplus`) which adds some processing levels\nto LLM's default HTML output.  Mathematical equations can be\ncompiled into SVG elements.  You can also generate PDF output\n(internally, this uses an instance of Chrome to print the\ngenerated HTML content to a PDF document).\n",
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
