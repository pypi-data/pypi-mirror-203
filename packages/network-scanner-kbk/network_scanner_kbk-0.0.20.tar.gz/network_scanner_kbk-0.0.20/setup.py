from setuptools import find_packages
import os
from distutils.core import setup

# User-friendly description from README.md
current_directory = os.path.dirname(os.path.abspath(__file__))
try:
    with open(os.path.join(current_directory, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()
except Exception:
    long_description = ''

setup(
	# Name of the package 
	name='network_scanner_kbk',
    package_dir = {'': 'src'},
	# Packages to include into the distribution 
	packages=["network_scanner_kbk", "network_scanner_kbk.tests"],
	# Start with a small number and increase it with 
	# every change you make https://semver.org 
	version='0.0.20',
	# Chose a license from here: https: // 
	# help.github.com / articles / licensing - a - 
	# repository. For example: MIT 
	license='MIT License',
	# Short description of your library 
	description='Project to scan and gather connectivity information on small networks',
	# Long description of your library 
	long_description=long_description,
	long_description_content_type='text/markdown',
	# Your name 
	author='Brian Kulig',
	# Your email 
	author_email='kbriankulig@gmail.com',
	# Either the link to your github or to your website 
	url='https://github.com/kbriankulig/network-scanner',
	# Link from which the project can be downloaded 
	download_url='',
	# List of keywords 
	keywords=[],
	# List of packages to install with this one 
	install_requires=[],
	# https://pypi.org/classifiers/ 
	classifiers=[]
)
