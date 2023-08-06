from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="pyfobal",
    version="0.1.2",
    packages= find_packages(),
    install_requires=[
        "requests",
    ],
    author="Karis Omotosho",
    author_email="karomo.sm@gmail.com",
    description="A Python SDK for the Fobal API",
    url="https://github.com/shonifari/pyfobal",
    long_description=long_description,
    long_description_content_type='text/markdown'
)
