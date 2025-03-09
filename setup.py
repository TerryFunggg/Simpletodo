from setuptools import setup

setup(
    name='todoapp',
    version='1.0',
    py_modules=['todo'],
    install_requires=[
        'prettytable',
        'termcolor',
    ],
    entry_points='''
        [console_scripts]
        todo=todo:main
    ''',
)

