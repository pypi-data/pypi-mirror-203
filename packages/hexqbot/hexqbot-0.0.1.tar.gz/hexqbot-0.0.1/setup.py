from setuptools import setup

with open("README.md", "r", encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='hexqbot',
    version='0.0.1',
    author='hexqbot',
    description='HexQBot API for Python',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author_email='slightwindsec@gmail.com',
    url='https://chat.hexqbot.xyz',
    packages=['hexqbot'],
    install_requires=[],
    entry_points={
        'console_scripts': [
        ]
    }
)