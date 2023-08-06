# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['oz_defender', 'oz_defender.relay']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'oz-defender',
    'version': '0.0.2',
    'description': '',
    'long_description': "# oz-defender\nPackage for interacting with Open Zeppelin's Defender API\n\n## Installation\nUsing `pip`\n```bash\npip install oz-defender\n```\n\nUsing `poetry`\n```bash\npoetry add oz-defender\n```\n\n## Usage\nblah blah\n\n## Contributing\n`oz-defender` is under active development so we welcome any and all contributions to improve the package!\n### Issues\nTo make it as simple as possible for us to help you, please include the following in:\n- OS\n- python version\n- `oz-defender` version\n\n### Pull requests\n**Note: Unless the change you're making is minor, please open an issue in GitHub to discuss a change before opening a PR**\n1. Clone this repository\n```bash\ngit clone https://github.com/franklin-systems/oz-defender\n```\n2. Install `pre-commit` and its hooks\n```bash\npip install pre-commit\n```\nor if you're using macOS\n```bash\nbrew install pre-commit\n```\nthen\n```bash\npre-commit install\n```\n3. Check out a new branch\n```bash\ngit checkout my-new-feature-branch\n```\n4. Commit and create your PR with a detailed description and tag the GitHub issue that your work addresses \n\n",
    'author': 'Franklin',
    'author_email': 'contact@hellofranklin.co',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/franklin-systems/oz-defender',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
