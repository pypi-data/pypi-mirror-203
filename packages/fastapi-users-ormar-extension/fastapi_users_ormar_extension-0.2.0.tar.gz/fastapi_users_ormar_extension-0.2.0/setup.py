# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fastapi_users_ormar_extension']

package_data = \
{'': ['*']}

install_requires = \
['fastapi-users>=10.2.0', 'ormar>=0.12.0,<0.13.0']

setup_kwargs = {
    'name': 'fastapi-users-ormar-extension',
    'version': '0.2.0',
    'description': 'Use ormar for your fastapi-users project.',
    'long_description': '# fastapi-users-ormar-ext\nExtension to use ormar in fastapi-users\n\n\n# Installation\n\nTo install use:\n```sh\npip install fastapi-users-ormar-extension\n```\n\n# Usage\n\nExample:\n\n```python\nfrom typing import Optional\n\nimport ormar\n\nfrom fastapi_users_ormar_extension import (\n    OrmarBaseUserTableUUID,\n    OrmarBaseOAuthAccountTableUUID,\n)\n\n\nclass BaseMeta(ormar.ModelMeta):\n    """Base metadata for models."""\n\n    database = database\n    metadata = meta\n\n\nclass User(OrmarBaseUserTableUUID):\n    class Meta(BaseMeta):\n        pass\n\n    phone: str = ormar.String(nullable=False, max_length=100)\n\n\nclass OAuthAccount(OrmarBaseOAuthAccountTableUUID):\n    class Meta(BaseMeta):\n        pass\n\n    user: User = ormar.ForeignKey(User, nullable=False, ondelete="cascade")\n```\n\n# TODO\n\n[ ] Think of a way to force `user` field overriding in OrmarBaseOAuthAccountTableUUID\n[ ] Add tests',
    'author': 'Jegor Kitskerkin',
    'author_email': 'jegor.kitskerkin@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
