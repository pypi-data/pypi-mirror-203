from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.2.2'
DESCRIPTION = 'Data fusion package for satellite data transformation.'
LONG_DESCRIPTION = 'Data fusion package for transforming L2 satellite to L3 spatial-temporal gridded data.'

# Setting up
setup(
    name = 'pyroscopegridding',         # Package name
    packages = ['pyroscopegridding'],   
    version = '0.2.2',      # Initial version
    license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description = 'Data fusion package for transforming L2 satellite to L3 spatial-temporal gridded data',  
    long_description = "file: README.md",
    author = 'Sally Zhao, Neil Gutkin',                 
    author_email = 'zhaosally0@gmail.com',     
    url = 'https://github.com/jwei-openscapes/aerosol-data-fusion',   # github repository  
    keywords = ['data fusion', 'satellite', 'L2', 'L3'],   # Keywords
    #packages = find_packages(),
    entry_points ={
        'console_scripts': [
            'pyroscopegridding = pyroscopegridding.gtools:main',
        ],
    },
    install_requires=[            
            'numpy',
            'joblib',
            #'cuda',
            'netCDF4',
            'pyhdf',
            'pyyaml',
            'numba',
            'argparse',
            'pandas'
        ],
    classifiers=[
    'Development Status :: 3 - Alpha',     
    'Intended Audience :: Developers',     
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',      #supported versions
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    ],
)