# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mechanical_bull', 'mechanical_bull.actions']

package_data = \
{'': ['*']}

install_requires = \
['bovine>=0.1.0,<0.2.0', 'tomli-w>=1.0.0,<2.0.0']

setup_kwargs = {
    'name': 'mechanical-bull',
    'version': '0.0.2.1',
    'description': 'A framework to automate reacting to ActivityStreams events.',
    'long_description': '# Mechanical Bull\n\nMechanical Bull is an ActivityPub Client application build based on [bovine](https://codeberg.org/helge/bovine/). It\'s main goal is to provide a platform for automating activities undertaking in the FediVerse. Furthermore, it serves as a demonstration how ActivityPub Clients can be build with bovine.\n\n## Installation\n\nOne can simply install mechanical_bull with pip via\n\n```bash\npip install mechanical-bull\n```\n\nOnce can then add a new user by running\n\n```bash\npython -m mechanical_bull.add_user\n```\n\nThis will then ask you to enter a name, the hostname, your ActivityPub Actor lives on, then prompt you to add a new did:key to your ActivityPub Actor. This did:key will be used to authenticate mechanical_bull against your server. Once you have added the key, press enter, and mechanical_bull is running. This method of authentication is called Moo-Auth-1 and described [here](https://blog.mymath.rocks/2023-03-15/BIN1_Moo_Authentication_and_Authoriation).\n\nThe configuration is saved in `config.toml`. bovine also supports authentication through private keys and HTTP signatures. For the details on how to configure this, please consult bovine. You can add further automations there.\n\nThen you should be able to run mechanical bull via\n\n```bash\npython -m mechanical_bull.run\n```\n\n## Writing automations\n\nThe examples of `mechanical_bull.actions.handle_follow_request` and `mechanical_bull.actions.log_to_file` should show how to write a new automation. The basic idea is that each file contains a function handle with signature\n\n```python\nasync def handle(client: BovineClient, data: dict, **kwargs):\n    return\n```\n\nhere the kwargs are the dict given by the definiton in the handler block, i.e.\n\n```toml\n[user.handlers]\n"my.package": { arg1 = "value1", arg2 = "value2 }\n```\n',
    'author': 'Helge',
    'author_email': 'helge.krueger@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://codeberg.org/helge/mechanical_bull',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
