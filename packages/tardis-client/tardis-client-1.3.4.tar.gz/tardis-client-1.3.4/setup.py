# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tardis_client', 'tardis_client.reconstructors']

package_data = \
{'': ['*']}

install_requires = \
['aiofiles>=0.8.0,<0.9.0',
 'aiohttp>=3.8.1,<4.0.0',
 'sortedcontainers>=2.1,<3.0']

setup_kwargs = {
    'name': 'tardis-client',
    'version': '1.3.4',
    'description': 'Python client for tardis.dev - historical tick-level cryptocurrency market data replay API.',
    'long_description': '# tardis-client\n\n[![PyPi](https://img.shields.io/pypi/v/tardis-client.svg)](https://pypi.org/project/tardis-client/)\n[![Python](https://img.shields.io/pypi/pyversions/tardis-client.svg)](https://pypi.org/project/tardis-client/)\n<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>\n\nPython client for [tardis.dev](https://tardis.dev) - historical tick-level cryptocurrency market data replay API.\nProvides fast, high level and developer friendly wrapper for more low level [HTTP API](https://docs.tardis.dev/api#http-api) with local file based caching build in.\n\n## Installation\n\nRequires Python 3.7.0+ installed.\n\n```sh\npip install tardis-client\n```\n\n## Usage\n\n```python\nimport asyncio\nfrom tardis_client import TardisClient, Channel\n\nasync def replay():\n    tardis_client = TardisClient()\n\n    # replay method returns Async Generator\n    # https://rickyhan.com/jekyll/update/2018/01/27/python36.html\n    messages = tardis_client.replay(\n        exchange="bitmex",\n        from_date="2019-06-01",\n        to_date="2019-06-02",\n        filters=[Channel(name="trade", symbols=["XBTUSD","ETHUSD"]), Channel("orderBookL2", ["XBTUSD"])],\n    )\n\n    # this will print all trades and orderBookL2 messages for XBTUSD\n    # and all trades for ETHUSD for bitmex exchange\n    # between 2019-06-01T00:00:00.000Z and 2019-06-02T00:00:00.000Z (whole first day of June 2019)\n    async for local_timestamp, message in messages:\n        # local timestamp is a Python datetime that marks timestamp when given message has been received\n        # message is a message object as provided by exchange real-time stream\n        print(message)\n\nasyncio.run(replay())\n```\n\n[![Try on repl.it](https://repl-badge.jajoosam.repl.co/try.png)](https://repl.it/@TardisThad/tardis-python-client-example)\n\n## API\n\n`tardis-client` package provides `TardisClient` and `Channel` classes.\n\n```python\nfrom tardis_client import TardisClient, Channel\n```\n\n### TardisClient\n\nOptional client constructor parameters.\n\n| name                   | type     | default value               | description                                                                                                                                                     |\n| ---------------------- | -------- | --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |\n| `api_key` (optional)   | `string` | `""`                        | optional `string` containing API key for [tardis.dev](https://tardis.dev) API. If not provided only first day of each month of data is accessible (free access) |\n| `cache_dir` (optional) | `string` | `<os.tmpdir>/.tardis-cache` | optional `string` with path to local dir that will be used as cache location. If not provided default `temp` dir for given OS will be used.                     |\n\nExample:\n\n```python\n# creates new client instance with access only to sample data (first day of each month)\ntardis_client = TardisClient()\n\n# creates new client with access to all data for given API key\ntardis_client = TardisClient(api_key="YOUR_API_KEY")\n\n# creates new client with custom cache dir\ntardis_client = TardisClient(cache_dir="./cache")\n```\n\n- ### `tardis_client.clear_cache()`\n\n  Removes local file cache dir and it\'s contents.\n\n  Example:\n\n  ```python\n  tardis_client = TardisClient()\n\n  tardis_client.clear_cache()\n  ```\n\n- ### `tardis_client.replay(exchange, from_date, to_date, filters=[])`\n\n  Replays historical market data messages for given replay arguments.\n\n  Returns [Async Generator](https://rickyhan.com/jekyll/update/2018/01/27/python36.html) with named tuples (`namedtuple("Response", ["local_timestamp", "message"])`).\n\n  - `local_timestamp` is a Python datetime object specyfying when message has been received from the exchange real-time data feed.\n\n  - `message` is Python dict with parsed JSON that has exactly the same format as message provided by particular exchange\'s real-time data feed.\n\n    #### `replay` method parameters:\n\n    | name                 | type                              | default value | description                                                                                                                                                                                       |\n    | -------------------- | --------------------------------- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |\n    | `exchange`           | `string`                          | -             | requested exchange name - Use [/exchanges](https://docs.tardis.dev/api/http#exchanges) API call to get allowed exchanges ids                                                                      |\n    | `from_date`          | `string`                          | -             | requested UTC start date of data feed - [valid ISO date string](https://docs.python.org/3/library/datetime.html#datetime.date.fromisoformat), eg: `2019-04-05` or `2019-05-05T00:00:00`           |\n    | `to_date`            | `string`                          | -             | requested UTC end date of data feed - [valid ISO date string](https://docs.python.org/3/library/datetime.html#datetime.date.fromisoformat), eg: `2019-04-05` or `2019-05-05T00:00:00`             |\n    | `filters` (optional) | [`List[Channel]`](#channel-class) | []            | optional filters of requested data feed. Use [/exchanges/:exchange](https://docs.tardis.dev/api/http#exchanges-exchange) API call to get allowed channel names and symbols for requested exchange |\n\n    ##### `Channel` class\n\n    `Channel` class constructor parameters.\n\n    | name      | type           | description                                                                                                                                         |\n    | --------- | -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |\n    | `name`    | `string`       | Use [/exchanges/:exchange](https://docs.tardis.dev/api#exchanges-exchange) API call to get allowed channel names and symbols for requested exchange |\n    | `symbols` | `List[string]` | Use [/exchanges/:exchange](https://docs.tardis.dev/api#exchanges-exchange) API call to get allowed channel names and symbols for requested exchange |\n\n    ```python\n    Channel(name="trade", symbols=["XBTUSD","ETHUSD"])\n    Channel("orderBookL2", ["XBTUSD"])\n    ```\n\n## FAQ\n\n#### How to debug it if something went wrong?\n\n`tardis-client` uses Python logging on `DEBUG` level for that purpose. In doubt please create issue in this repository with steps how to reproduce the issue.\n\n#### Where can I find more details about tardis.dev API?\n\nCheck out [API docs](https://docs.tardis.dev/api).\n\n## License\n\nMPL-2.0\n',
    'author': 'Thad',
    'author_email': 'thad@tardis.dev',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/tardis-dev/python-client',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7',
}


setup(**setup_kwargs)
