#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from setuptools import setup, find_packages

# those lines for preprocessing
# f.e.
# sed -i "s/^__dev_suffix__ = ''/__dev_suffix__ = '.dev'/g" setup.py
# sed -i "s/^__dev_build__ = ''/__dev_build__ = '${BUILD_NUMBER}'/g" setup.py
__dev_suffix__ = ''  # commonly ".dev"
__dev_build__ = ''   # commonly pipeline number


def long_description():
    with open("README.md", "r") as fh:
        return fh.read()


setup(
    name="videonoise",
    version="0.3" + __dev_suffix__ + __dev_build__,
    description='Videonoise - util for generate a white noise video with audio.',
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "videonoise=videonoise.videonoise:main",
        ],
    },
    install_requires=[
        "numpy",
        "pydub",
        "moviepy",
    ],
    long_description=long_description(),
    long_description_content_type='text/markdown',
    url='https://github.com/ph20/videonoise',
    author='Alexander Grynchuk',
    author_email='agrynchuk@gmail.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires=">=3.6",
    project_urls={
        'Bug Reports': 'https://github.com/ph20/videonoise/issues',
        'Source': 'https://github.com/ph20/videonoise/',
    },
)
