#!/usr/bin/env python3

from pathlib import Path
from setuptools import setup

directory = Path(__file__).resolve().parent

setup(name='docs_mini',
      version='0.0.1',
      description='mini documents ai',
      author='BB',

      packages = ['docs_mini'],
      classifiers=[
        "Programming Language :: Python :: 3",
      ],
      install_requires=[
        "flask",
      ],
      python_requires='>=3.8',
      extras_require={},
      include_package_data=True)
