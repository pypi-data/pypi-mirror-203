# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src',
 'curses_wrapper': 'src/curses_wrapper',
 'kafka_wrapper': 'src/kafka_wrapper'}

packages = \
['cli', 'curses_wrapper', 'kafka_wrapper']

package_data = \
{'': ['*']}

install_requires = \
['confluent-kafka>=2.0.2,<3.0.0', 'pyyaml>=6.0,<7.0', 'tabulate>=0.9.0,<0.10.0']

entry_points = \
{'console_scripts': ['k4 = cli.main:cli']}

setup_kwargs = {
    'name': 'k4',
    'version': '0.1.0a0',
    'description': 'A command line tool for controlling and interacting with Kafka.',
    'long_description': '# K4\n\nK4 is a terminal based UI to interact with your Kafka clusters.\n\n## Roadmap\n\nkafka_wrapper\n\n- [ ] acl\n- [x] broker\n- [x] test broker\n- [ ] consume\n- [x] consumer groups/offsets\n- [x] test consumer groups/offsets\n- [ ] partition\n- [ ] producer\n- [x] topic\n- [x] test topic\n\nk4\n\n- [ ] ~/.config/k4config\n- [ ] 10 bit custom colors\n- [x] windows\n    - [x] command input\n    - [x] scrolling - https://github.com/mingrammer/python-curses-scroll-example\n    - [x] resizing\n- [x] screen\n- [ ] screen manager\n- [ ] content row edit\n- [ ] content row describe\n- [x] poc edit ini config using default terminal editor. see examples/kafka_wrapper/topics.py\n\n\n## Wish List\n\n- producer\n- consumer\n- schema registry\n- kafka connect\n- query JMX metrics for and display to users. disk size, bytes-in, bytes-out, etc.\n    - https://github.com/dgildeh/JMXQuery/tree/master/python\n\n## Install\n\n```bash\npip install k4\n```\n\n## Examples\n\n```\nTODO\n```\n\n## License\n\n[Apache 2.0 License - aidanmelen/k4](https://github.com/aidanmelen/k4/blob/main/README.md)',
    'author': 'Aidan Melen',
    'author_email': 'aidan-melen@protonmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/aidanmelen/k4',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
