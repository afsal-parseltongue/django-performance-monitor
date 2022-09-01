import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-performance-monitor',
    url='https://github.com/afsal-parseltongue/django-performance-monitor',
    version='0.2.0',
    packages=find_packages(),
    include_package_data=True,
    description='A simple django applications to log the response time greater than a threshold value',
    long_description=README,
    long_description_content_type="text/markdown",
    author='Afsal Salim',
    author_email='afsal@parseltongue.co.in',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.8',
)
