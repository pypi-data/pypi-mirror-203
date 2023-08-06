from setuptools import setup

setup(

name='riyazi',

version = '0.17'

)


with open('README.md', encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

def configuration(parent_package='', top_path=None):
    from numpy.distutils.misc_util import Configuration
    config = Configuration('riyazi', parent_package, top_path)
    return config

if __name__ == "__main__":
    from numpy.distutils.core import setup

    config = configuration(top_path='').todict()
    setup(**config)




"""
from setuptools import setup, find_packages

setup(
    name='riyazi',
    packages=find_packages(),
    version = 0.5
    
)
"""
