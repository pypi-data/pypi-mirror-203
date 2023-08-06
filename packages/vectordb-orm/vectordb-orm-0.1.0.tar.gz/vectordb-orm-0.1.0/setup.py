# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['vectordb_orm', 'vectordb_orm.tests']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.24.2,<2.0.0', 'protobuf>=4.22.3,<5.0.0', 'pymilvus>=2.2.6,<3.0.0']

setup_kwargs = {
    'name': 'vectordb-orm',
    'version': '0.1.0',
    'description': '',
    'long_description': "# vectordb-orm\n\n`vectordb-orm` is an Object-Relational Mapping (ORM) library designed to work with vector databases, such as Milvus. The project aims to provide a consistent and convenient interface for working with vector data, allowing you to interact with vector databases using familiar ORM concepts and syntax.\n\n## Getting Started\n\nHere are some example code snippets demonstrating common behavior with vectordb-orm. vectordb-orm is designed around python typehints. You create a class definition by subclassing `MilvusBase` and providing typehints for the keys of your model, similar to pydantic. These fields also support custom initialization behavior if you want (or need) to modify their configuration options.\n\n| Field Type      | Description                                                                                                                                                                                                                                |\n|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|\n| BaseField       | The `BaseField` provides the ability to add a default value for a given field. This should be used in cases where the more specific field types aren't relevant.                                                                           |\n| PrimaryKeyField | The `PrimaryKeyField` is used to specify the primary key of your model, and one is required per class.                                                                                                                                     |\n| VarCharField    | The `VarCharField` is used to specify a string field, and the `EmbeddingField` is used to specify a vector field.                                                                                                                          |\n| EmbeddingField  | The `EmbeddingField` also supports specifying an index type, which is used to specify the index type for the field. The `EmbeddingField` also supports specifying a dimension, which is used to specify the dimension of the vector field. |\n\n### Object Definition\n\n```python\nfrom vectordb_orm import MilvusBase, EmbeddingField, VarCharField, PrimaryKeyField\nfrom pymilvus import Milvus\nfrom vectordb_orm.indexes import IVF_FLAT\nimport numpy as np\n\nclass MyObject(MilvusBase):\n    __collection_name__ = 'my_object_collection'\n\n    id: int = PrimaryKeyField()\n    text: str = VarCharField(max_length=128)\n    embedding: np.ndarray = EmbeddingField(dim=128, index=IVF_FLAT(cluster_units=128))\n```\n\n## Querying Syntax\n\n```python\nfrom vectordb_orm import MilvusSession\n\n# Instantiate a MilvusSession\nsession = MilvusSession()\n\n# Perform a simple boolean query\nresults = session.query(MyObject).filter(MyObject.text == 'bar').limit(2).all()\n\n# Rank results by their similarity to a given reference vector\nquery_vector = np.array([8.0]*128)\nresults = session.query(MyObject).filter(MyObject.text == 'bar').order_by_similarity(MyObject.embedding, query_vector).limit(2).all()\n```\n\n## Installation\n\nTo get started with vectordb-orm, simply install the package and its dependencies, then import the necessary modules:\n\n```bash\npip install vectordb-orm\n```\n\nWe use poetry for local development work:\n\n```bash\npoetry install\npoetry run pytest\n```\n\n## Why use an ORM?\n\nMost vector databases use a JSON-like querying syntax where schemas and objects are specified as dictionary blobs. This makes it difficult to use IDE features like autocomplete or typehinting, and also can lead to error prone code while translating between Python logic and querying syntax.\n\nAn ORM provides a high-level, abstracted interface to work with databases. This abstraction makes it easier to write, read, and maintain code, as well as to switch between different database backends with minimal changes. Furthermore, an ORM allows developers to work with databases in a more Pythonic way, using Python objects and classes instead of raw SQL queries or low-level API calls.\n\n## Comparison to SQLAlchemy\n\nWhile vectordb-orm is inspired by the widely-used SQLAlchemy ORM, it is specifically designed for vector databases, such as Milvus. This means that vectordb-orm offers unique features tailored to the needs of working with vector data, such as similarity search, index management, and efficient data storage. Although the two ORMs share some similarities in terms of syntax and structure, vectordb-orm focuses on providing a seamless experience for working with vector databases.\n\n## WIP\n\nPlease note that vectordb-orm is still a (somewhat large) work in progress. The current implementation focuses on Milvus integration, the goal is to eventually expand support to other vector databases. Contributions and feedback are welcome as we work to improve and expand the capabilities of vectordb-orm.\n",
    'author': 'Pierce Freeman',
    'author_email': 'pierce@freeman.vc',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
