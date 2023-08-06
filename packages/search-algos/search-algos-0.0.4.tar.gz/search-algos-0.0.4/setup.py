from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='search-algos',
    version='0.0.4',
    description='A collection of searching algorithms for lists and dictionaries',
    author='Arpan Adhikari',
    author_email='codewitharpan@gmail.com',
    url='https://github.com/arpan45/search-algos-pypi',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages()
)
