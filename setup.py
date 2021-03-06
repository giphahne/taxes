from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='py_cost_basis',
    version='0.0.1',
    description='computes cost basis',
    author='Dan Hahne',
    author_email='contact@danhahne.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: System Tools',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='taxes tax cost basis',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=[
        'argcomplete',
    ],
    entry_points={
        'console_scripts': [
            'costbasis-compute=py_cost_basis:main',
            'costbasis-ingest=py_cost_basis:ingest',
            'costbasis-dedup=py_cost_basis:dedup',
        ],
    },
)
