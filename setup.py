#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
from setuptools import setup


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding='utf-8').read()

requirements = []
with open('requirements.txt') as f:
    for line in f:
        stripped = line.split("#")[0].strip()
        if len(stripped) > 0:
            requirements.append(stripped)
# https://github.com/pypa/setuptools_scm
use_scm = {"write_to": "napari_mri/_version.py"}

setup(
    name='napari-mri',
    author='SUSMITA SAHA',
    author_email='susmi06@yahoo.com',
    description='A simple plugin to use with napari for 3D-viewing of Magnetic Resonance Imaging file formats',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    python_requires='>=3.7',
    install_requires=["napari_plugin_engine>=0.1.4","nibabel", "numpy"],
    setup_requires=['setuptools_scm'],
    use_scm_version=use_scm,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Framework :: napari',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: BSD License',
    ],
    entry_points={
        'napari.plugin': [
            'napari-mri = napari_mri.nifty_reader',
        ],
    },
)
