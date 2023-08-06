# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['poectrl',
 'poectrl.api',
 'poectrl.api.managers',
 'poectrl.api.resources',
 'poectrl.api.schemas',
 'poectrl.api.schemas.request',
 'poectrl.api.schemas.response']

package_data = \
{'': ['*']}

install_requires = \
['fastapi[all]>=0.88,<0.96', 'paramiko>=2.12,<4.0', 'typer[all]>=0.7.0,<0.8.0']

entry_points = \
{'console_scripts': ['poectrl = poectrl.main:app']}

setup_kwargs = {
    'name': 'poectrl',
    'version': '0.4.0',
    'description': 'Control PoE status on select Ubiquiti switches',
    'long_description': '# Control PoE status on a Ubiquiti TS-8-Pro Switch <!-- omit in toc -->\n\n[![PyPI version](https://badge.fury.io/py/poectrl.svg)](https://badge.fury.io/py/poectrl)\n\n**Development work** for a system to remotely and automatically control the PoE\nstatus of individual ports on multiple Ubiquiti TS-8-Pro Switch, using\npredefined profiles.\n\nThis has currently only been tested on the TS-8-PRO ToughSwitch routers,\nthough others will be added soon.\n\n**IMPORTANT: This library DOES NOT (and CAN NOT) ensure that any device attached\nto a port is compatible with the voltage selected. BE VERY CAREFUL that you\nchoose the correct voltage for your devices or you can DAMAGE THEM. No\nresponsibility is taken for equipment damaged using this library.**\n\n- [Status](#status)\n- [Use Cases](#use-cases)\n- [Installation](#installation)\n- [Configuration](#configuration)\n- [Usage](#usage)\n  - [As a command-line program](#as-a-command-line-program)\n  - [As an API](#as-an-api)\n    - [API Routes](#api-routes)\n- [Development Plans](#development-plans)\n- [Contributing](#contributing)\n\n## Status\n\nThis project is in no way ready to be used, and documentation is non-existent.\nSee the Development Plans below. Until I have a stable useful interface, check\nthe source code if you are interested 😃\n\n## Use Cases\n\n- Control a set of PoE-powered IP cameras, switches and access points to allow\ndisabling when not needed or quick enabling if required.\n\n## Installation\n\nThe latest version is uploaded to [pypi.org](https://pypi.org) so you can\ninstall this the same as any other package:\n\n```console\npip install poectrl\n```\n\n## Configuration\n\n**IMPORTANT : The configuration layout has CHANGED from version 1.2.0. If you\nare using config files from previous versions you will need to update the\n"devices" section to fit the below schema and change the profile to point to the\nname instead of IP address.**\n\nThe program is configured using a `poectrl.json` file either in the current\nworking directory (first priority) or the user\'s home directory. This is a\nsimple file that describes all devices and profiles. There is an example in\n[poectrl-example.json](poectrl-example.json) :\n\n```json\n{\n  "devices": {\n    "switch_1": {"ip": "192.168.0.187", "user": "ubnt", "password": "ubnt"},\n    "switch_2": {"ip": "192.168.0.190", "user": "ubnt", "password": "ubnt"}\n  },\n  "profiles": {\n    "cctv_on": {\n      "switch_1": {"4": 24, "5": 24, "8": 48},\n      "switch_2": {"5": 24, "6": 24, "7": 48}\n    },\n    "cctv_off": {\n      "switch_1": {"4": 0, "5": 0, "8": 0},\n      "switch_2": {"5": 0, "6": 0, "7": 0}\n    }\n  }\n}\n\n```\n\n## Usage\n\n### As a command-line program\n\nApply a predefined profile, setting the PoE port voltages.\n\n```console\n$ poectrl apply cctv_off\nUsing configuration from /home/seapagan/data/work/own/poectrl/poectrl.json\nConncting to switch_1 (192.168.0.187):\n  Setting port 4 to 0V\n  Setting port 5 to 0V\n  Setting port 8 to 0V\nConncting to switch_2 (192.168.0.190):\n  Setting port 5 to 0V\n  Setting port 6 to 0V\n  Setting port 7 to 0V\n\n```\n\nList all defined profiles:\n\n```console\n$ poectrl list\nUsing configuration from /home/seapagan/data/work/own/ts-8-pro-control/poectrl.json\n\nValid profiles are :\n - cctv_on\n - cctv_off\n```\n\nShow settings for a profile :\n\n```console\n$ poectrl show cctv_off\nUsing configuration from /home/seapagan/data/work/own/ts-8-pro-control/poectrl.json\n{\n    "switch_1": {\n        "4": 0,\n        "5": 0,\n        "8": 0\n    },\n    "switch_2": {\n        "5": 0,\n        "6": 0,\n        "7": 0\n    }\n}\n```\n\n### As an API\n\nIt is also possible to run this locally as an API, which can then allow easier\ncontrol using a web browser.\n\n**Important**: This is only designed for local network use, not over the\ninternet since there is NO access control set up. If you open this to the\ninternet then ANYONE can control your PoE!\n\n```console\n$ poectrl serve\nINFO:     Started server process [49922]\nINFO:     Waiting for application startup.\nINFO:     Application startup complete.\nINFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)\n```\n\nThere are a couple of command-line switches you can use :\n\n`---refresh` - This is useful if you are modifiying or troubleshooting the code,\nthe API will reload after each source code change.\n\n`--port <int>` - Change the port that the API listens on (default is 8000)\n\n`--host` - binds to all network interfaces on the host, allowing access from\nother machines using the public IP address of this machine\n\nAfter this, you can access the API on `http://localhost:8000`. Swagger docs are\navailable at `http://localhost:8000/docs`\n\n#### API Routes\n\nThere are currently 3 routes which correspond to the same command in the CLI.\n\n`/list/` - Lists all the defined profiles\\\n`/show/{profile_name}` - Shows details for the specific profile\\\n`/apply/{profile_name}` - Apply the specific profile\n\n## Development Plans\n\nCurrent proposed project plan.\n\n- [x] Write proof-of-concept code to control ports.\n- [x] Refactor and tidy the above code into a Library Class.\n- [x] Create a basic CLI using this Library\n- [x] Continue the CLI to use a config file, show current values, list profiles\n  etc.\n- [x] Publish on PyPi as a standalone package.\n- [x] Wrap this into an API (using FastAPI) for local use only.\n- [ ] Create a Web App to interface with the above API.\n\n## Contributing\n\nAt this time, the project is barely in it\'s planning stage but I do have a firm\nidea where it\'s going and how to structure it. As such, other contributions are\nnot looked for at this time. Hopefully, within a few days this project will be\nat a much more advanced stage and that will change 😃.\n',
    'author': 'Grant Ramsay',
    'author_email': 'seapagan@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/seapagan/ts-8-pro-control',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7.2,<4.0',
}


setup(**setup_kwargs)
