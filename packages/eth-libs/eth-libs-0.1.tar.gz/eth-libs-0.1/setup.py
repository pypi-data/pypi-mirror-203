from setuptools import setup, find_packages


setup(
    name='eth-libs',
    version='0.1',
    license='MIT',
    author="Xavier Rodriguez",
    packages=find_packages('src'),
    package_dir={'': 'src'},
    keywords='eth-libs',
    install_requires=[
          'requests', 'web3',
      ],

)