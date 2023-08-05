# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['kisskh_downloader', 'kisskh_downloader.enums', 'kisskh_downloader.models']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0',
 'pydantic>=1.10.5,<2.0.0',
 'requests>=2.28.2,<3.0.0',
 'validators>=0.20.0,<0.21.0',
 'yt-dlp>=2023.2.17,<2024.0.0']

entry_points = \
{'console_scripts': ['kisskh = kisskh_downloader.cli:kisskh']}

setup_kwargs = {
    'name': 'kisskh-downloader',
    'version': '0.1.5',
    'description': 'Simple downloaded for https://kisskh.co/',
    'long_description': '# :tv: kisskh-dl\n\n<div align="center">\n   <img src="https://i.imgur.com/nhQtOZa.png">\n   <br>\n   <strong><i>Simple downloaded for https://kisskh.co/</i></strong>\n   <br>\n   <a href="https://pypi.org/project/kisskh-downloader/">\n   <img src="https://img.shields.io/pypi/v/kisskh-downloader?style=for-the-badge">\n   </a>\n   <img src="https://img.shields.io/github/actions/workflow/status/Dibakarroy1997/kisskh-dl/pull-request.yml?style=for-the-badge">\n   <img src="https://img.shields.io/pypi/dm/kisskh-downloader?style=for-the-badge">\n</div>\n\n---\n\n👋 Welcome to the kisskh-downloader README! This package is a simple command-line tool for downloading shows from https://kisskh.co/. Here\'s everything you need to know to get started:\n\n## 💻 Installation\n\nTo install kisskh-downloader, simply run the following command:\n\n```console\npip install -U kisskh-downloader\n```\n\n## 📚 Usage\n\nAfter installing the package, you can use the `kisskh dl` command to download shows from the command line.\n\n```console\nkisskh dl --help\nUsage: kisskh dl [OPTIONS] DRAMA_URL_OR_NAME\n\nOptions:\n  -f, --first INTEGER             Starting episode number.\n  -l, --last INTEGER              Ending episode number.\n  -q, --quality [360p|480p|540p|720p|1080p]\n                                  Quality of the video to be downloaded.\n  -s, --sub-langs TEXT            Languages of the subtitles to download.\n  -o, --output-dir TEXT           Output directory where downloaded files will\n                                  be store.\n  --help                          Show this message and exit.\n```\n\nHere are some examples:\n\n### 🔗 Direct download entire series in highest quality available in current folder\n\n```console\nkisskh dl "https://kisskh.co/Drama/Island-Season-2?id=7000" -o .\n```\n\n![Download all using URL](https://i.imgur.com/cvKYqK3.gif)\n\n\n### 🔍 Search and download entire series in highest quality available in current folder\n\n```console\nkisskh dl "Stranger Things" -o .\n1. Stranger Things - Season 4\n2. Stranger Things - Season 1\n3. Stranger Things - Season 2\n4. Stranger Things - Season 3\nPlease select one from above: 1\n```\n\n![Download all using URL](https://i.imgur.com/mLPqjgj.gif)\n\n### ⬇️ Download specific episodes with specific quality\n\n> :exclamation: Note that if the selected quality is not available, it will try to get something lower than that quality. If that also is not available, it will try to get the best quality available.\n\nDownloads episode 4 to 8 of `Alchemy of Souls` in 720p:\n```console\nkisskh dl "https://kisskh.co/Drama/Alchemy-of-Souls?id=5043" -f 4 -l 8 -q 720p -o .\n```\n\n![Download range of episodes](https://i.imgur.com/Q6697pa.gif)\n\nDownloads episode 3 of `A Business Proposal` in 720p:\n```console\nkisskh dl "https://kisskh.co/Drama/A-Business-Proposal?id=4608" -f 3 -l 3 -q 720p -o .\n```\n\n![Download single episode](https://i.imgur.com/cNlED8m.gif)\n\nYou can also dowload single episode by providing the episode URL\n\n```console\nkisskh dl "https://kisskh.co/Drama/A-Business-Proposal/Episode-3?id=4608&ep=86439&page=0&pageSize=100" -o .\n```\n\nFor more options, use the `--help` flag.\n\n---\n\n# 🐞 DEBUG\n\nTo enable debugging, use the `-vv` flag while running `kisskh dl`.\n\n```console\nkisskh -vv dl "https://kisskh.co/Drama/A-Business-Proposal?id=4608" -f 3 -l 3 -q 720p\n```\n\n---\n\n# :construction: TODO\n- [ ] Add ability to export all download link\n- [ ] Add ability to open stream in some player\n',
    'author': 'Debakar Roy',
    'author_email': 'allinonedibakar@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
