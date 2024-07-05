import os
from setuptools import setup, find_packages

cwd = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(cwd, 'requirements.txt')) as f:
    reqs = f.read().splitlines()

setup(
    name='styletts2',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=reqs,
)
