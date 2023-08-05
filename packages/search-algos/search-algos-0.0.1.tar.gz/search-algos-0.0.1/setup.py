from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='search-algos',
    version='0.0.1',
    description='A collection of searching algorithms for lists and dictionaries',
    author='Arpan Adhikari',
    author_email='codewitharpan@gmail.com',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages()
)
