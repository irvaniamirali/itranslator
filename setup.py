from distutils.core import setup
from setuptools import find_packages


setup(
    name='itranslator',
    packages=find_packages('.'),
    version='0.0.1',
    license='MIT',
    description='A Python package to use in translating texts based on api',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_context_type='text/markdown',
    author='amirali irvany',
    author_email='dev.amirali.irvany@gmail.com',
    url='https://github.com/metect/itranslator',
    keywords=['translate', 'translator', 'google', 'google-translate', 'free-translator'],
    install_requires=['requests', 'user_agent'],
)
