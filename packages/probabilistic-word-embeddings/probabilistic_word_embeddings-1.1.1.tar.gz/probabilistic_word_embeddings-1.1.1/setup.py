# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['probabilistic_word_embeddings']

package_data = \
{'': ['*'], 'probabilistic_word_embeddings': ['data/eval/*']}

install_requires = \
['networkx',
 'pandas',
 'progressbar2',
 'scikit-learn',
 'tensorflow-probability>=0.11,<0.12',
 'tensorflow>=2.2,<3.0']

setup_kwargs = {
    'name': 'probabilistic-word-embeddings',
    'version': '1.1.1',
    'description': 'Probabilistic Word Embeddings for Python',
    'long_description': '# probabilistic-word-embeddings v0.15.1\n\nProbabilistic Word Embedding module for Python. Built with TensorFlow 2.x and TensorFlow probability.\n\n[Documentation is available here.](https://ninpnin.github.io/probabilistic-word-embeddings/)\n\n## Colab demo\n\nA demo of the project can be run on [Google Colab](https://colab.research.google.com/drive/1dGqWn7SMqg-fGzVUGzXSOUmsX8m9k5k2).\n',
    'author': 'Your Name',
    'author_email': 'you@example.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/ninpnin/probabilistic-word-embeddings',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
