# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['flm_citations', 'flm_citations.citesources']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=6.0,<7.0',
 'arxiv>=1.4.2,<2.0.0',
 'backoff>=2.1.2,<3.0.0',
 'citeproc-py>=0.6.0,<0.7.0',
 'flm-core>=0.3.0a10',
 'requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'flm-citations',
    'version': '0.2.4',
    'description': 'Support for citations in FLM (see flm package)',
    'long_description': 'None',
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
