# setup.py
from setuptools import setup, find_packages

setup(
    name='learning-apis',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # Dependências do projeto
    ],
    extras_require={
        'utils': ['my_utils']
    }
)
