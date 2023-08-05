#!/usr/bin/env python
import os
from setuptools import setup


version = '0.0.3'


def read(f):
    return open(os.path.join(os.path.dirname(__file__), f)).read().strip()


setup(name='talqual',
      version=version,
      description=('TAL Chameleon (static site generator)'),
      long_description='\n\n'.join((read('README.rst'), read('CHANGES.txt'))),
      classifiers=[
          'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
          'Intended Audience :: Developers',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Development Status :: 1 - Planning',
          'Topic :: Internet :: WWW/HTTP',
      ],
      author='Aleix Llusà Serra',
      author_email='timbaler@timbaler.cat',
      url='https://gitlab.com/timbaler/talqual/',
      project_urls={
        'Documentation': 'https://gitlab.com/timbaler/talqual/',
        'Source': 'https://gitlab.com/timbaler/talqual/',
        'Tracker': 'https://gitlab.com/timbaler/talqual/issues',
      },
      license='GPLv3+',
      packages=['talqual'],
      entry_points="""
          [console_scripts]
          talqual=talqual.cli:cli
      """,
      python_requires='>=3.9',
      install_requires=[
          'importlib-metadata ~= 1.0 ; python_version < "3.8"',
          'anytree',
          'chameleon',
          'click',
          'docutils',
          'pyyaml',
          ],
      extras_require={
        'multilingual': [
            'babel',
            'babel-lingua-chameleon',
        ],
        'test': [
            'sphinx',
            'pytest',
            'pytest-html',
            'pytest-cov',
            'coverage-conditional-plugin',
            'pytest-flake8',
            'flake8<4', # https://github.com/tholo/pytest-flake8/issues/81
            'pytest-mock',
            'pytest-selenium',
            'flake8-isort',
            'transcrypt',
        ],
      },
      include_package_data=True
      )
