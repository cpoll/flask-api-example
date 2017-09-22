# -*- coding: utf-8 -*-

from pip.req import parse_requirements
from pip.download import PipSession
from setuptools import setup

links = []
requires = []
requirements_filename = 'requirements-to-freeze.txt'
requirements = parse_requirements(requirements_filename,
                                    session=PipSession())
for item in requirements:
    if getattr(item, 'link', None):
        links.append(str(item.link))
    if item.req:
        requires.append(str(item.req))

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='flask-api-example',
    version='0.1.0',
    description='Generic Flask App',
    long_description=readme,
    author='Cristian Poll',
    author_email='cristian@cristianpoll.com',
    url='https://github.com/cpoll/flask-api-example',
    license=license,
    packages=["api"],
    install_requires=requires,
    dependency_links=links,
    setup_requires=['green'],
)
