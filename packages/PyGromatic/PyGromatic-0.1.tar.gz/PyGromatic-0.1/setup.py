from setuptools import setup, find_packages


setup(
    name='PyGromatic',
    version='0.1',
    license='MIT',
    author="Joris Dalderup",
    author_email='joris@jorisdalderup.nl',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/jorissoris/PyGromatic',
    keywords='example project',
    install_requires=[
          'matplotlib',
          'numpy',
          'MDAnalysis'
      ],

)