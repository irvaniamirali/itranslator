from setuptools import setup, find_packages


with open('README.md', encoding='UTF-8') as file:
    readme = file.read()

setup(
    name='itranslator',
    version='0.0.3',
    author='amirali irvany',
    author_email='dev.amirali.irvany@gmail.com',
    description='A Python package to use in translating texts based on api',
    keywords=['translate', 'translator', 'google', 'google-translate', 'free-translator', 'asyncio'],
    long_description=readme,
    python_requires="~=3.7",
    long_description_content_type='text/markdown',
    url='https://github.com/metect/itranslator',
    packages=find_packages(),
    exclude_package_data={'': ['*.pyc', '*__pycache__*']},
    install_requires=['requests', 'user_agent'],
    classifiers=[
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
