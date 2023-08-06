from setuptools import setup, find_packages


setup(
    name='eth-decoder',
    version='1.1',
    license='MIT',
    author="Xavier Rodriguez",
    packages=find_packages('src'),
    package_dir={'': 'src'},
    keywords='eth-decoder',
    install_requires=[
          'requests', 'web3',
      ],

)