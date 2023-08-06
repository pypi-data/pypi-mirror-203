# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['feynmodel', 'feynmodel.interface', 'feynmodel.model']

package_data = \
{'': ['*']}

install_requires = \
['deprecated',
 'deprecation',
 'particle',
 'smpl_doc',
 'smpl_io',
 'smpl_util',
 'ufo_mssm',
 'ufo_sm',
 'xsdata[cli,lxml,soap]']

setup_kwargs = {
    'name': 'feynmodel',
    'version': '0.0.4',
    'description': 'Models for constructing Feynman diagrams',
    'long_description': '# FeynModel\n\nFeynModel is a project to develop an XML dialect for describing Feynman Models.\nIt is in design very close to the UFO format, but not as restrictive (-> less complete).\n\n[![PyPI version][pypi image]][pypi link] [![PyPI version][pypi versions]][pypi link]  ![downloads](https://img.shields.io/pypi/dm/feynml.svg)\n\n\n[![test][a t image]][a t link]     [![Coverage Status][c t i]][c t l] [![Codacy Badge][cc c i]][cc c l]  [![Codacy Badge][cc q i]][cc q l]  [![Documentation][rtd t i]][rtd t l]\n\n## Installation\n```sh\npip install [--user] feynmodel\n```\n\nor from cloned source:\n\n```sh\npoerty install --with docs --with dev\npoetry shell\n```\n\n## Documentation\n\n*   <https://pyfeyn2.readthedocs.io/en/stable/feynml/>\n*   <https://apn-pucky.github.io/pyfeyn2/feynml/index.html>\n\n## Related:\n\n*   <https://github.com/APN-Pucky/feynml>\n*   <https://github.com/APN-Pucky/pyfeyn2>\n\n\n## Development\n\n\n### package/python structure:\n\n*   <https://mathspp.com/blog/how-to-create-a-python-package-in-2022>\n*   <https://www.brainsorting.com/posts/publish-a-package-on-pypi-using-poetry/>\n\n[doc stable]: https://apn-pucky.github.io/feynmodel/index.html\n[doc test]: https://apn-pucky.github.io/feynmodel/test/index.html\n\n[pypi image]: https://badge.fury.io/py/feynmodel.svg\n[pypi link]: https://pypi.org/project/feynmodel/\n[pypi versions]: https://img.shields.io/pypi/pyversions/feynmodel.svg\n\n[a t link]: https://github.com/APN-Pucky/feynmodel/actions/workflows/test.yml\n[a t image]: https://github.com/APN-Pucky/feynmodel/actions/workflows/test.yml/badge.svg\n\n[cc q i]: https://app.codacy.com/project/badge/Grade/6604fe515a7e4ebf927b44f8f5f79dc0\n[cc q l]: https://www.codacy.com/gh/APN-Pucky/feynmodel/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=APN-Pucky/feynmodel&amp;utm_campaign=Badge_Grade\n[cc c i]: https://app.codacy.com/project/badge/Coverage/6604fe515a7e4ebf927b44f8f5f79dc0\n[cc c l]: https://www.codacy.com/gh/APN-Pucky/feynmodel/dashboard?utm_source=github.com&utm_medium=referral&utm_content=APN-Pucky/feynmodel&utm_campaign=Badge_Coverage\n\n[c t l]: https://coveralls.io/github/APN-Pucky/feynmodel?branch=master\n[c t i]: https://coveralls.io/repos/github/APN-Pucky/feynmodel/badge.svg?branch=master\n\n[rtd t i]: https://readthedocs.org/projects/pyfeyn2/badge/?version=latest\n[rtd t l]: https://pyfeyn2.readthedocs.io/en/latest/?badge=latest\n',
    'author': 'Alexander Puck Neuwirth',
    'author_email': 'alexander@neuwirth-informatik.de',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/APN-Pucky/feynmodel',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
