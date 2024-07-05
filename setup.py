import os
import subprocess
from setuptools import setup, find_packages, Command

cwd = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(cwd, 'requirements_setup.txt')) as f:
    reqs = f.read().splitlines()

class PostInstallCommand(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            subprocess.check_call(['python', '-m', 'unidic', 'download'])
            subprocess.check_call(['pip', 'install', 'git+https://github.com/resemble-ai/monotonic_align.git'])
        except subprocess.CalledProcessError as e:
            print("Failed to execute a command: ", e)

setup(
    name='styletts2',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=reqs,
    cmdclass={
        'install': PostInstallCommand,
    },
)
