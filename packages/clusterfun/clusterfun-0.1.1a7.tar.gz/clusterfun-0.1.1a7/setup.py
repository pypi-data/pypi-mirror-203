# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['clusterfun',
 'clusterfun.models',
 'clusterfun.plot_types',
 'clusterfun.storage',
 'clusterfun.storage.local',
 'clusterfun.utils']

package_data = \
{'': ['*'],
 'clusterfun': ['frontend/*',
                'frontend/404/*',
                'frontend/_next/static/1QyiY8tsv4hAH3HR9ReVe/*',
                'frontend/_next/static/chunks/*',
                'frontend/_next/static/chunks/pages/*',
                'frontend/_next/static/chunks/pages/plots/*',
                'frontend/_next/static/chunks/pages/plots/[uuid]/*',
                'frontend/_next/static/chunks/pages/plots/[uuid]/media/*',
                'frontend/_next/static/css/*',
                'frontend/_next/static/media/*']}

install_requires = \
['boto3',
 'fastapi',
 'orjson',
 'pandas',
 'pillow',
 'pyarrow',
 'requests',
 'uvicorn']

entry_points = \
{'console_scripts': ['clusterfun = clusterfun.serve_cli:main']}

setup_kwargs = {
    'name': 'clusterfun',
    'version': '0.1.1a7',
    'description': 'Clusterfun - a plotting library to inspect data',
    'long_description': '# Clusterfun\n\nExplore data with one line of code. \n\n\nClusterfun is a python plotting library to explore data in your plots.\nAfter installing clusterfun with `pip install clusterfun`\n\nSee https://clusterfun.app for documentation and examples.',
    'author': 'Jochem Gietema',
    'author_email': 'jochem@giete.ma',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8.1',
}


setup(**setup_kwargs)
