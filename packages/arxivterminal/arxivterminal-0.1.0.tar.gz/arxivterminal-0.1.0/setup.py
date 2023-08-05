# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['arxivterminal']

package_data = \
{'': ['*']}

install_requires = \
['appdirs>=1.4.4,<2.0.0',
 'arxiv>=1.4.3,<2.0.0',
 'bs4>=0.0.1,<0.0.2',
 'click>=8.1.3,<9.0.0',
 'lxml>=4.9.2,<5.0.0',
 'openai>=0.27.4,<0.28.0',
 'pydantic>=1.10.7,<2.0.0',
 'requests>=2.28.2,<3.0.0',
 'termcolor>=2.2.0,<3.0.0']

entry_points = \
{'console_scripts': ['arxiv = arxivterminal.cli:cli']}

setup_kwargs = {
    'name': 'arxivterminal',
    'version': '0.1.0',
    'description': 'An application for summarizing Arxiv results within the terminal',
    'long_description': '# Arxiv Terminal\n![Tests](https://github.com/jbencina/arxivterminal/actions/workflows/main.yaml/badge.svg)\n\nArxiv Terminal is a command-line interface (CLI) tool for fetching, searching, and displaying papers from the [arXiv](https://arxiv.org/) preprint repository. The tool allows you to fetch papers from specified categories, search the fetched papers, and display their statistics.\n\n## Features\n\n- Fetch paper abstracts from specified categories and save them in a local sqllite database.\n- Show fetched papers and interatively open for more detailed abstracts\n- Search fetched papers based on a query.\n\n## Installation\n\n```bash\npip install arxivterminal\n```\n\n## Usage\n\nThe CLI is invoked using the `arxiv` command, followed by one of the available commands:\n\n- `arxiv fetch [--num-days] [--categories]`: Fetch papers from the specified categories and store them in the database.\n- `arxiv delete_all`: Delete all papers from the database.\n- `arxiv show [--days-ago]`: Show papers fetched from the specified number of days ago.\n- `arxiv stats`: Show statistics of the papers stored in the database.\n- `arxiv search <query>`: Search papers in the database based on a query.\n\n### Examples\n\nFetch papers from the "cs.AI" and "cs.CL" categories from the last 7 days:\n\n```bash\narxiv fetch --num-days 7 --categories cs.AI,cs.CL\n```\n\nDelete all papers from database:\n\n```bash\narxiv delete_all\n```\n\nShow papers fetched in the last 7 days\n\n```bash\narxiv show --days-ago 7\n```\n\nDisplay statistics of the papers stored in the database:\n\n```bash\narxiv stats\n```\n\nShow papers containing the phrase "deep learning":\n\n```bash\narxiv search "deep learning"\n```\n',
    'author': 'John Bencina',
    'author_email': 'jbencina@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
