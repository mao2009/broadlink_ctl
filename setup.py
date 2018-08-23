from setuptools import setup
import sys

requires = ['broadlink']
if sys.version_info.major == 2:
    requires.append('configparser')
setup(
    name='rmctl',
    version='0.1.1',
    packages={'pkg'},
    install_requires=requires,
    entry_points={
        'console_scripts': [
            'rmctl = pkg.broadlink_ctl:main',
        ],
    },
    url='',
    license='',
    author='mao2009',
    author_email='',
    description='Simple cli client for broadlink'
)
