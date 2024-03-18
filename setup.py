from distutils.core import setup
from setuptools import find_packages
import os


current_directory = os.path.dirname(os.path.abspath(__file__))
try:
    with open(os.path.join(current_directory, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()
except Exception:
    long_description = 'Translation of various texts without restrictions and without the need for authentication, token, access key, etc'


setup(
    name='itranslator',
    packages=find_packages('.'),
    version='0.0.1',
    license='MIT',
    description='A Python package to use in translating texts based on api',
    long_description=long_description,
    long_description_context_type='text/markdown',
    author='amirali irvany',
    author_email='dev.amirali.irvany@gmail.com',
    url='https://metect.github.io',
    download_url='https://github.com/metect/itranslator',
    keywords=['translate', 'translator', 'google', 'google-translate', 'free-translator'],
    install_requires=['requests', 'user_agent'],
)
