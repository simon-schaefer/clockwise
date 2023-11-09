from setuptools import setup, find_packages


REQUIRED = ['loguru']

setup(
    name='clockwise',
    version='1.0.0',
    description='A simple timing library for Python.',
    author='Simon Schaefer',
    author_email='simon.k.schaefer@gmail.com',
    packages=find_packages(),
    install_requires=REQUIRED,
    python_requires='>=3.0'
)
