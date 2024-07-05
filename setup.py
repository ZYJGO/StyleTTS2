from setuptools import setup, find_packages

with open('requirements.txt') as f:
    reqs = f.read().splitlines()

setup(
    name='styletts2',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=reqs,
)
