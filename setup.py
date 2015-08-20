# -*- coding: utf-8 -*-
import io
from setuptools import setup, find_packages

description = """
A django pipeline compiler to transform React in Coffeescript and Browserify.
"""

setup(
    name='django-pipeline-cjsx',
    version='0.1.0',
    description=description,
    long_description=io.open('README.md', encoding='utf-8').read(),
    author='Nick011',
    url='https://github.com/Nick011/django-pipeline-cjsx',
    packages=find_packages(),
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
    ]
)
