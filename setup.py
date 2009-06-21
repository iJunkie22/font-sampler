#!/usr/bin/env python

import os
from distutils.core import setup
import py2exe
setup(
    console=['font_list_generator.py', 'font_list_generator_gui.py'],

    #classifiers=?? 	#a list of classifiers 	list of strings 	(4)
    #download_url='http://',
    #platforms=[],  #multiplatform - don't limit it
    author='Shula Amokshim',
    author_email='shula.amokshim@gmx.com',
    description='generate font catalogs',
    license='GPL v3',
    long_description='generate font catalogs',
    maintainer='Shula Amokshim',
    maintainer_email='shula.amokshim@gmx.com',
    name='Font-Sampler',
    url='http://code.google.com/p/font-sampler',
    version='1.0',
    requires='wxPython',

    data_files=[
        ('bitmaps', []),
        ('config', []),
    ]

)
