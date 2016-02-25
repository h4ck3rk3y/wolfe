#!/usr/bin/env python

import os

from setuptools import setup, find_packages

if os.environ.get('USER', '') == 'vagrant':
  del os.link


setup(
  name='wolfe',
  version='0.0.5',
  description='i am winston wolfe, i solve problems',
  long_description=open('README.rst').read(),
  author='Gyanendra Mishra',
  author_email='anomaly.the@gmail.com',
  license='MIT',
  keywords=['wolfe', 'bugs', 'errrors', 'stackoverflow', 'cli', 'google'],
  url='https://github.com/h4ck3rk3y/wolfe',
  packages=find_packages(exclude=['contrib', 'docs', 'tests']),
  install_requires=[
    'docopt>=0.6.2',
    'requests>=2.6.0',
    'tabulate==0.7.5'
  ],
  entry_points={
    'console_scripts': [
        'wolfe = wolfe.wolfe:main'
    ],
  }
)