from setuptools import setup, find_packages
import codecs
import os

VERSION = '1.2.4'
DESCRIPTION = 'Umjunsik Programming Language'
LONG_DESCRIPTION = 'First esoteric programming language uniquely designed around a single individual\'s name for coding purposes.'

# Setting up
setup(
  name = 'umjunsik',
  version = VERSION,
  author = 'rycont',
  author_email = 'rycont@outlook.kr',
  description = DESCRIPTION,
  long_description_content_type = 'text/markdown',
  long_description = LONG_DESCRIPTION,
  packages = find_packages(),
  install_requires = [],
  keywords = ['esolang', 'meme', 'umjunsik'],
  url = 'https://github.com/rycont/umjunsik-lang',
  license = 'MIT',
  classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11',
  ],
)