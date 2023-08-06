# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['resolver']

package_data = \
{'': ['*']}

entry_points = \
{'sceptre.resolvers': ['from_json = resolver.from_json:FromJsonResolver',
                       'to_json = resolver.to_json:ToJsonResolver']}

setup_kwargs = {
    'name': 'sceptre-json-resolver',
    'version': '0.1.0',
    'description': 'A Sceptre resolver to serialize and deserialize json',
    'long_description': '# sceptre-json-resolver\n\nA Sceptre resolver to serialize and deserialize json.\n\n## Motivation\n\nThere are use cases where you may want to pass in either a string\nor a json object to a cloudformation or sceptre_user_data parameter.\nThis simple resolver can take some json and serialize it or deserialize\nit before passing it into a cloudformation parameter or a\nscepter_user_data parameter.\n\n## Installation\n\nTo install directly from PyPI\n```shell\npip install sceptre-json-resolver\n```\n\nTo install from this git repo\n```shell\npip install git+https://github.com/Sceptre/sceptre-json-resolver.git\n```\n\n## Usage/Examples\n\n```yaml\nparameters|sceptre_user_data:\n  <name>: !from_json [ <string> ]\n\nparameters|sceptre_user_data:\n  <name>: !to_json [ <json object> ]\n```\n\n__NOTE__: This resolver expects a single-item list argument.\n\n## Basic Examples\n\nTake some json object serialize it to a string then pass it to a parameter:\n```yaml\nparameters:\n   myparam: !to_json [{"key": "value"}]\n```\n__Note__: The string `\'{"key": "value"}\'` is passed to myparam\n\n\nTake a string deserialize it to a json object then pass it to a parameter:\n```yaml\nsceptre_user_data:\n  myparam: !from_json [\'{"key": "value"}\']\n```\n__Note__: The object `{"key": "value"}` is passed to myparam\n\n\n## Nested resolver examples\n\nThese use case requires the nested resolver feature in\nSceptre version 4.1 and greater.\n\n\nLoad a json object from a file using the\n[sceptre file resolver](https://pypi.org/project/sceptre-file-resolver/),\nserialize the object to a string then pass it to a parameter:\n```yaml\nparameters:\n  hounds: !to_json [ !file \'hounds.json\' ]\n```\n\n\nMake a request to a REST API using the\n[sceptre-request-resolver](https://pypi.org/project/sceptre-request-resolver/),\ndeserialize the response to a json object then pass it to a parameter:\n```yaml\nsceptre_user_data:\n  hounds: !from_json\n    - !request \'https://dog.ceo/api/breed/hound/list\'\n```\n',
    'author': 'Sceptre',
    'author_email': 'sceptreorg@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/Sceptre/sceptre-json-resolver',
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<3.12',
}


setup(**setup_kwargs)
