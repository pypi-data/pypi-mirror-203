# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pylatexenc',
 'pylatexenc.latex2text',
 'pylatexenc.latexencode',
 'pylatexenc.latexnodes',
 'pylatexenc.latexnodes.parsers',
 'pylatexenc.latexwalker',
 'pylatexenc.macrospec',
 'pylatexenc.macrospec._pyltxenc2_argparsers']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['latex2text = pylatexenc.latex2text.__main__:main',
                     'latexencode = pylatexenc.latexencode.__main__:main',
                     'latexwalker = pylatexenc.latexwalker.__main__:main']}

setup_kwargs = {
    'name': 'pylatexenc',
    'version': '3.0a14',
    'description': 'Simple LaTeX parser providing latex-to-unicode and unicode-to-latex conversion',
    'long_description': "pylatexenc\n==========\n\nSimple LaTeX parser providing latex-to-unicode and unicode-to-latex conversion\n\n.. image:: https://img.shields.io/github/license/phfaist/pylatexenc.svg?style=flat\n   :target: https://github.com/phfaist/pylatexenc/blob/master/LICENSE.txt\n\n.. image:: https://img.shields.io/pypi/v/pylatexenc.svg?style=flat\n   :target: https://pypi.org/project/pylatexenc/\n\nPython: ≥ 3.4 or ≥ 2.7. The library is designed to be as backwards-compatible as\nreasonably possible and is able to run on old python verisons should it be\nnecessary. (Use the setup.py script directly if you have python<3.7, poetry\ndoesn't seem to work with old python versions.)\n\n\nUnicode Text to LaTeX code\n--------------------------\n\nThe ``pylatexenc.latexencode`` module provides a function ``unicode_to_latex()``\nwhich converts a unicode string into LaTeX text and escape sequences. It should\nrecognize accented characters and most math symbols. A couple of switches allow\nyou to alter how this function behaves.\n\nYou can also run ``latexencode`` in command-line to convert plain unicode text\n(from the standard input or from files given on the command line) into LaTeX\ncode, written on to the standard output.\n\nA third party plug-in for Vim\n`vim-latexencode <https://github.com/Konfekt/vim-latexencode>`_\nby `@Konfekt <https://github.com/Konfekt>`_\nprovides a corresponding command to operate on a given range.\n\n\nParsing LaTeX code & converting to plain text (unicode)\n-------------------------------------------------------\n\nThe ``pylatexenc.latexwalker`` module provides a series of routines that parse\nthe LaTeX structure of given LaTeX code and returns a logical structure of\nobjects, which can then be used to produce output in another format such as\nplain text.  This is not a replacement for a full (La)TeX engine, rather, this\nmodule provides a way to parse a chunk of LaTeX code as mark-up code.\n\nThe ``pylatexenc.latex2text`` module builds up on top of\n``pylatexenc.latexwalker`` and provides functions to convert given LaTeX code to\nplain text with unicode characters.\n\nYou can also run ``latex2text`` in command-line to convert LaTeX input (either\nfrom the standard input, or from files given on the command line) into plain\ntext written on the standard output.\n\n\nDocumentation\n-------------\n\nFull documentation is available at https://pylatexenc.readthedocs.io/.\n\nTo build the documentation manually, run::\n\n  > poetry install --with=builddoc\n  > cd doc/\n  doc> poetry run make html\n\n\nLicense\n-------\n\nSee LICENSE.txt (MIT License).\n\nNOTE: See copyright notice and license information for file\n``tools/unicode.xml`` provided in ``tools/unicode.xml.LICENSE``.  (The file\n``tools/unicode.xml`` was downloaded from\nhttps://www.w3.org/2003/entities/2007xml/unicode.xml as linked from\nhttps://www.w3.org/TR/xml-entity-names/#source.)\n",
    'author': 'Philippe Faist',
    'author_email': 'philippe.faist@bluewin.ch',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
