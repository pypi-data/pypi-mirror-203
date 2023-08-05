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
    'version': '0.1.1a6',
    'description': 'Clusterfun - a plotting library to inspect data',
    'long_description': '# Clusterfun\n\nClusterfun is a tool for visualizing data and media in a browser. It\'s built on top of [Plotly](https://plotly.com).\nThe goal is to make it easy to visualize data and media in a browser, without having to write much code.\n\n## Usage\n\n### Plot types\n\nThe following plot types are available:\n\n- [Scatter](#scatter)\n- [Histogram](#histogram)\n- [Grid](#grid)\n- [Violin](#violin)\n- [Pie chart](#pie)\n\n```python\nimport clusterfun as clt\n```\n\n#### Scatter\n\n```python\nclt.scatter(df, x="x", y="y", media="img_path")\n```\n\nExample\n\n#### Histogram\n\n```python\nclt.histogram(df, x="x", media="img_path", bins=50)\n```\n\nExample\n\n#### Grid\n\nA simple grid of media, no plot. Useful for inspecting data when no underlying numbers are available yet.\n\n```python\nclt.grid(df, media="img_path")\n```\n\nExample\n\n#### Violin\n\n```python\nclt.violin(df, y="y", media="img_path")\n```\n\nExample\n\n#### Pie chart\n\n```python\nclt.pie(df, x="x", y="y", media="img_path")\n```\n\nExample\n\n### Parameters\n\n#### Media\n\nThe media column in the dataframe will be used to load the media.\n\n#### Color\n\nYou can color different categories with the `color` parameter.\n\n- The `color` can be either a color name or hex value\n\n#### Bounding box\n\nBounding boxes can be added with the `bounding_box` parameter.\nA bounding box cell in a dataframe needs to contain a dictionary or a list of dictionaries with bounding box values: `xmin, ymin, xmax, ymax, label (optional), color (optional)`. <br />\nExample of a bounding box:\n\n```python\nbounding_box = {\n    "xmin": 12,\n    "ymin": 10,\n    "xmax": 100,\n    "ymax": 110,\n    "color": "green",\n    "label": "ground truth"\n}\n```\n\n- The bounding box coordinates can be either floats or integers.\n\n## Filtering\n\nData in plots can be filtered to quickly find subsets of the data you\'re interested in.\n\n## Installation\n\n### Python library\n\nYou can create plots that open in your browser by installing the Python library:\n\n```bash\npip install clusterfun\n```\n\n### Data loading\n\nClusterfun supports S3 and local data storage and loading. The media column in the dataframe will be used to determine where to load the media from.\n',
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
