from setuptools import setup

setup(
    name='animals',
    entry_points={
        'console_scripts': [
            'animals=animals.__main__:main'
        ],
        'animals': [
            'cat=animals.models:Cat',
            'dog=animals.models:Dog',
        ],
    }
)