from setuptools import setup, find_packages

setup(
    name='python-library-30140721',
    version='1.5.0',
    author= 'naina-gupta',
    author_email='nainag077@gmail.com',
    description= 'python library which includes linear, nodes, and trees',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'numpy',
        'scipy'
    ],
)