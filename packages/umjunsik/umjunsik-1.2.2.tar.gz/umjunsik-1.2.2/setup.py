from distutils.core import setup

setup(
  name = 'umjunsik',
  packages = ['umjunsik'],
  version = '1.2.2',
  license = 'MIT',
  description = 'Umjunsik programming language',
  author = 'rycont',
  author_email = 'rycont@outlook.kr',
  url = 'https://github.com/rycont/umjunsik-lang',
  include_dirs = ['umjunsik'],
  keywords = ['ESOLANG'],
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