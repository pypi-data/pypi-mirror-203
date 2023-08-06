# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['shapleyrouting', 'shapleyrouting.rideshare']

package_data = \
{'': ['*']}

install_requires = \
['geopy>=2.3.0,<3.0.0', 'numpy>=1.24.2,<2.0.0', 'streamlit>=1.20.0,<2.0.0']

setup_kwargs = {
    'name': 'shapleyrouting',
    'version': '0.1.0',
    'description': 'An implementation of efficient Shapley value calculation of routing problem',
    'long_description': '# Shapley-Routing\n\nDocumentation can be found [here](https://joshzwiebel.github.io/Shapley-Routing/build/html/index.html).\n\n## Installation\n\n:one: Install [Poetry](https://python-poetry.org/):\n\n```bash\npip install poetry\n```\n\nIf you encounter an error, try:\n\n```bash\nexport PATH="/home/<user>/.local/bin:$PATH"\n```\n\n:two: Install dependencies:\n\n```bash\npoetry install\n```\n\n## Testing\n\n### Run style check\n\n```bash\npoetry run flake8 .\npoetry run black .\n```\n\n### Running unit tests\n\n```bash\npoetry run pytest -v .\n```\n\n### Running unit tests with coverage\n\n```bash\npoetry run coverage run -m pytest -v .\npoetry run coverage report -m\n```\n\n## Docs\n\nDocs can be built using the following commands:\n\n```bash\ncd docs/\npoetry run make html\n```\n',
    'author': 'Connor Sweet',
    'author_email': 'cssweet@uwaterloo.ca',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8, !=2.7.*, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, !=3.5.*, !=3.6.*, !=3.7.*',
}


setup(**setup_kwargs)
