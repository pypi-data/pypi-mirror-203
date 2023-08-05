from __future__ import division, print_function
from setuptools import setup


_version = '0.1'

setup(name='seawolf',
      version=_version,
      description='Tools for plots',
      author='Bayron Torres Gordillo',
      author_email='torres.bayron@gmail.com',
      install_requires=['numpy','pandas','seaborn','matplotlib'],
      packages=['seawolf'],
      include_package_data=True,
      license = 'BSD',
      platforms = ["Windows", "Linux", "Solaris", "Mac OS-X", "Unix"],
      python_requires='>=3.5'
    )