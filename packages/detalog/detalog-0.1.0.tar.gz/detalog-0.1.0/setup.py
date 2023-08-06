# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['detalog']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.28.2,<3.0.0']

setup_kwargs = {
    'name': 'detalog',
    'version': '0.1.0',
    'description': 'Logger for awesome Deta Space applications based on awesome PingBack events aggregator',
    'long_description': '# DetaLog\n\nDetaLog is a Python package that provides a logging handler for sending logs to a [PingBack](https://github.com/MaximilianHeidenreich/PingBack) events crawler. This can be useful for aggregating logs from multiple sources into a central place, and analyzing them to gain insights about your application or system.\n\n## Installation\n\nYou can install DetaLog via pip:\n\n```\npip install detalog\n```\n\n## Usage\n\nHere\'s an example of how to use DetaLog in your Python code:\n\n```python\nimport logging\nfrom detalog import PingBackHandler\n\napp_url = "https://my-pingback-events-crawler.com"\napi_key = "my-api-key"\n\nlogger = logging.getLogger(__name__)\nlogger.setLevel(logging.INFO)\n\nhandler = PingBackHandler(app_url, api_key, project="my-project", channel="my-channel")\nhandler.setLevel(logging.INFO)\n\nlogger.addHandler(handler)\n\nlogger.info("Hello, world!")\n\nlogger.debug("Hello, world!", extra={"channel": "debug-channel", "project": "my-project-2"})\n```\n\nIn this example, we create a logger with the name `__name__`, which is the name of the current module. We set its logging level to `INFO`, which means it will log messages at the `INFO` level or above. We also create a `PingBackHandler` instance, passing in the URL of the PingBack events crawler, an API key for authentication, and optional `project` and `channel` parameters to specify the destination of the logs. We set the handler\'s logging level to `INFO` as well, so it will only handle messages at that level or above.\n\nFinally, we add the handler to the logger, and log an `INFO` message with the text "Hello, world!". This message will be sent to the PingBack events crawler via the handler\'s `emit` method, in the form of a JSON payload.\n\n## License\n\nDetaLog is licensed under the MIT License. See LICENSE for details.\n',
    'author': 'mamsdeveloper',
    'author_email': 'butvin.mihail@yandex.ru',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
