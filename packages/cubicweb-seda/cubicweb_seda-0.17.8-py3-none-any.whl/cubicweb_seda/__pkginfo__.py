# pylint: disable=W0622
"""cubicweb-seda application packaging information"""

modname = 'seda'
distname = 'cubicweb-seda'

numversion = (0, 17, 8)
version = '.'.join(str(num) for num in numversion)

license = 'LGPL'
author = 'LOGILAB S.A. (Paris, FRANCE)'
author_email = 'contact@logilab.fr'
description = 'Data Exchange Standard for Archival'
web = 'http://www.cubicweb.org/project/%s' % distname

__depends__ = {
    'cubicweb': '>= 3.26',
    'cubicweb-eac': '>= 0.8.4',
    'cubicweb-skos': '>= 2.0.0',
    'cubicweb-compound': '>= 0.7',
    'cubicweb-relationwidget': '>= 0.4',
    'cubicweb-squareui': None,
    'pyxst': '>= 0.3.2',
    'rdflib': '>= 4.1, < 6.0.0',
}
__recommends__ = {}

classifiers = [
    'Environment :: Web Environment',
    'Framework :: CubicWeb',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3 :: Only',
    'Programming Language :: JavaScript',
]
