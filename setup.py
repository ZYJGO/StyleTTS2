from setuptools import setup, find_packages

with open('requirements.txt.lock') as f:
    reqs = f.readlines()

requirements = []
for req in reqs:
    req = req.strip()
    if req and not req.startswith('#'):
        requirements.append(req.split(' ')[0])

setup(
    name='styletts2',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
)
