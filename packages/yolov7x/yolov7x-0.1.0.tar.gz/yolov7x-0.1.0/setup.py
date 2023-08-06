# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['yolov7x']

package_data = \
{'': ['*']}

install_requires = \
['ipython>=8.12.0,<9.0.0',
 'matplotlib>=3.2.2',
 'numpy>=1.18.5,<1.24.0',
 'opencv-python>=4.1.1',
 'pandas>=1.1.4',
 'pillow>=7.1.2',
 'protobuf<4.21.3',
 'psutil>=5.9.5,<6.0.0',
 'pyyaml>=5.3.1',
 'requests>=2.23.0',
 'scipy>=1.4.1',
 'seaborn>=0.11.0',
 'tensorboard>=2.4.1',
 'thop>=0.1.1.post2209072238,<0.2.0',
 'torch>=1.7.0,!=1.12.0',
 'torchvision>=0.8.1,!=0.13.0',
 'tqdm>=4.41.0']

setup_kwargs = {
    'name': 'yolov7x',
    'version': '0.1.0',
    'description': '',
    'long_description': '',
    'author': 'Your Name',
    'author_email': 'you@example.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
