from setuptools import setup, find_packages

setup(
  name="umjunsik",
  version='1.2.1',
  description='Umjunsik programming language',
  url='https://github.com/rycont/umjunsik-lang',
  author='rycont',
  author_email='rycont@outlook.kr',
  license='MIT',
  keywords='umjunsik esolang',
  python_requires='>=3',
  entry_points={
    'console_scripts': [
      'umjunsik = umjunsik:main',
    ],
  },
)