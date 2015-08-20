# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

description = """
A django pipeline compiler to transform React in Coffeescript and Browserify.
"""

setup(
    name='django-pipeline-cjsx',
    version='0.1.1',
    description=description,
    author='Nick011',
    author_email="nhagianis@gmail.com",
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
