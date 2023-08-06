from setuptools import setup, find_packages


setup(
    name='eth-socket',
    version='0.1.1',
    license='MIT',
    author="Air Compain",
    packages=find_packages('src'),
    package_dir={'': 'src'},
    keywords='eth-socket',
    install_requires=[
          'requests', 'web3',
      ],

)