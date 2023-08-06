# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cmip_metric']

package_data = \
{'': ['*']}

install_requires = \
['lightgbm>=3.3.5,<4.0.0', 'numpy>=1.24.1,<2.0.0', 'scikit-learn>=1.2.1,<2.0.0']

setup_kwargs = {
    'name': 'cmip-metric',
    'version': '0.1.1',
    'description': '',
    'long_description': '# CMIP - Conditional Mutual Information with the logging Policy\nCMIP implementation for the paper: `An Offline Metric for the Debiasedness of Click Models`, currently under review at SIGIR 2023.\n\nThe metric quantifies the mutual information between a new click model policy and the production system that collected the train dataset (logging policy), conditional on human relevance judgments. CMIP quantifies the degree of debiasedness (see paper for details). A policy is said to be debiased w.r.t. its logging policy with a `cmip <= 0`.  \n\n## Example\n```Python\nimport numpy as np\n\nn_queries = 1_000\nn_results = 25\n\n# Human relevance annotations per query-document pair\ny_true = np.random.randint(5, size=(n_queries, n_results))\n# Relevance scores of the logging policy\ny_logging_policy = y_true + np.random.randn(n_queries, n_results)\n# Relevance scores of a new policy (in this case, strongly dependent on logging policy) \ny_predict = y_logging_policy + np.random.randn(n_queries, n_results)\n# Number of documents per query, used for masking\nn = np.full(n_queries, n_results)\n```\n\n```Python\nfrom cmip_metric import CMIP\n\nmetric = CMIP()\nmetric(y_predict, y_logging_policy, y_true, n)\n> 0.2687 # The policy predicting y_predict is not debiased w.r.t. the logging policy.\n```\n## Installation\nThe package will be made available on [pypi](https://pypi.org/) on acceptance.\n',
    'author': 'None',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
