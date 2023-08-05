from setuptools import setup, find_packages


setup(
    name='eth_py',
    version='2.0',
    license='MIT',
    author="Xavier Rodriguez",
    packages=find_packages('src'),
    package_dir={'': 'src'},
    keywords='eth_py',
    install_requires=[
          'requests', 'web3',
      ],

)