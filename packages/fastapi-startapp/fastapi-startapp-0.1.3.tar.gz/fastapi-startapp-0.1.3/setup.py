# -*-coding:utf-8-*-
from setuptools import (
    setup
)


setup(
    version='0.1.3',
    name='fastapi-startapp',
    install_requires=['click'],
    descritption='fastapi startapp',
    include_package_data=True,
    packages=['scripts', 'core'],
    entry_points='''
        [console_scripts]
        startapp=scripts.startapp:cli
    ''',
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Operating System :: OS Independent',
    ]
)
