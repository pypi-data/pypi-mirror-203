from setuptools import setup, find_packages

setup(
    name='python-library-30153653',
    version='1.5.0',
    author= 'arsalan_khaleel',
    author_email='arsalan.khaleel@ucalgary.ca',
    description= 'python library which includes linear, nodes, and trees. Made by Arsalan Khaleel 30153653 ',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'numpy',
        'scipy'
    ],
)
