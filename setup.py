#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import find_packages, setup

EXCLUDE_FROM_PACKAGES = ["build", "dist", "test"]

# read version number from version.txt, otherwise alpha version
# Github CI can create version.txt dynamically.
def get_version(fname):
    if os.path.exists(fname):
        with open(fname, 'r') as f:
            version = f.readline().strip()
    else:
        version = '0.1'

    return version

# Load README.md for long description
def load_long_description(fname):
    if os.path.exists(fname):
        with open(fname, 'r') as f:
            long_description = f.read()
    else:
        long_description = 'Parse PDF file with PyMuPDF and generate docx with python-docx.'

    return long_description

def load_requirements(fname):
    try:
        # pip >= 10.0
        from pip._internal.req import parse_requirements        
    except ImportError:
        # pip < 10.0
        from pip.req import parse_requirements

    reqs = parse_requirements(fname, session=False)
    try:
        requirements = [str(ir.requirement) for ir in reqs]
    except AttributeError:
        requirements = [str(ir.req) for ir in reqs]

    return requirements

setup(
    name="pdf2docxnogui",    
    version=get_version('version.txt'),
    keywords=["pdf-to-word", "pdf-to-docx"],
    description="parse PDF files to docx",
    long_description=load_long_description('README.md'),
    long_description_content_type='text/markdown',
    license="GPL v3", 
    author="dothinking",
    author_email="train8808@gmail.com",
    url="https://github.com/dothinking/pdf2docxnogui",
    packages=find_packages(exclude=EXCLUDE_FROM_PACKAGES),
    include_package_data=True,    
    zip_safe=False,
    install_requires=load_requirements("requirements.txt"),
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "pdf2docxnogui=pdf2docxnogui.main:main"
            ]},
)
