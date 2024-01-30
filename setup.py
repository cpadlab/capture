from setuptools import setup

setup(
    name='Capture!ByPass',
    version='1.23.1',
    description='This script automates the process of bypassing login credentials in a CTF environment, Specifically designed for the "Capture this!" CTF room on TryHackMe.',
    url='https://github.com/14wual/capture',
    author='Carlos Padilla Labella',
    license='GPL-3.0 license',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Operating System :: POSIX :: Linux',
    ],
    install_requires=[
        'argparse==1.4.0',
        'importlib-metadata==4.12.0',
        'requests==2.31.0',
        'beautifulsoup4==4.12.2',
        'colorama==0.4.6'
    ],
    project_urls={
        'Source': 'https://github.com/14wual/capture/blob/main/bypass.py',
    },
)