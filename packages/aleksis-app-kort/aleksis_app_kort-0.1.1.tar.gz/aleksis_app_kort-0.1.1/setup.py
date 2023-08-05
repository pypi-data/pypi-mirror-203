# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aleksis',
 'aleksis.apps.kort',
 'aleksis.apps.kort.migrations',
 'aleksis.apps.kort.templatetags']

package_data = \
{'': ['*'],
 'aleksis.apps.kort': ['frontend/*',
                       'frontend/messages/*',
                       'locale/*',
                       'locale/ar/LC_MESSAGES/*',
                       'locale/de_DE/LC_MESSAGES/*',
                       'locale/fr/LC_MESSAGES/*',
                       'locale/la/LC_MESSAGES/*',
                       'locale/nb_NO/LC_MESSAGES/*',
                       'locale/ru/LC_MESSAGES/*',
                       'locale/tr_TR/LC_MESSAGES/*',
                       'locale/uk/LC_MESSAGES/*',
                       'static/*',
                       'templates/kort/*',
                       'templates/kort/card/*',
                       'templates/kort/card_layout/*',
                       'templates/kort/printer/*',
                       'templates/material/fields/*']}

install_requires = \
['aleksis-core>=3.0b2,<4.0',
 'django-ace>=1.0.12,<2.0.0',
 'django-formtools>=2.3,<3.0',
 'python-barcode>=0.14.0,<0.15.0']

entry_points = \
{'aleksis.app': ['kort = aleksis.apps.kort.apps:DefaultConfig']}

setup_kwargs = {
    'name': 'aleksis-app-kort',
    'version': '0.1.1',
    'description': 'AlekSIS (School Information System)\u200a—\u200aApp Kort (manage student IDs)',
    'long_description': 'AlekSIS (School Information System)\u200a—\u200aApp Kort (manage student IDs)\n==================================================================================================\n\nAlekSIS\n-------\n\nThis is an application for use with the `AlekSIS®`_ platform.\n\nFeatures\n--------\n\nThe author of this app did not describe it yet.\n\nLicence\n-------\n\n::\n\n  Copyright © 2021, 2022 Jonathan Weth <dev@jonathanweth.de>\n  Copyright © 2021 Margarete Grassl <grasslma@katharineum.de>\n\n  Licenced under the EUPL, version 1.2 or later\n\nPlease see the LICENCE.rst file accompanying this distribution for the\nfull licence text or on the `European Union Public Licence`_ website\nhttps://joinup.ec.europa.eu/collection/eupl/guidelines-users-and-developers\n(including all other official language versions).\n\n.. _AlekSIS®: https://edugit.org/AlekSIS/AlekSIS\n.. _European Union Public Licence: https://eupl.eu/\n',
    'author': 'Margarete Grassl',
    'author_email': 'grasslma@katharineum.de',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://aleksis.org',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
