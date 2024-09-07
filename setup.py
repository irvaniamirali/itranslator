from setuptools import setup, find_packages


with open('README.md', encoding='UTF-8') as file:
    readme = file.read()

setup(
    name='itranslator',
    version='3.0',
    author='AmirAli Irvani',
    author_email='social.irvaniamirali@gmail.com',
    description='Text translation package based on Google Translate API ',
    keywords=['translate', 'translator', 'google', 'google-translate', 'free-translator', 'asyncio'],
    long_description=readme,
    python_requires="~=3.7",
    long_description_content_type='text/markdown',
    url='https://github.com/irvaniamirali/itranslator',
    packages=find_packages(),
    exclude_package_data={'': ['*.pyc', '*__pycache__*']},
    install_requires=['httpx', 'user_agent'],
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
