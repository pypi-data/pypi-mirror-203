import requests
from setuptools import setup, find_packages
def versions(package_name):
    data = requests.get(f'https://pypi.python.org/pypi/{package_name}/json')
    _versions = data.json()['releases'].keys()
    return list(_versions)[-1]


package_version = versions('novalabs-backtest')
VERSION = package_version[:-1] + str(int(package_version[-1])+1)

with open("README.md", "r") as fh:
    long_description = fh.read()
    
with open('requirements.txt', 'r') as file:
    requirements = file.read().replace('\n', ' ')

dependencies = requirements.split()

setup(
    name="novalabs-backtest",
    version="1.1.11",
    author="Nova Labs",
    author_email="devteam@novalabs.ai",
    description="Wrappers around Nova Labs utilities focused on safety and testability.",
    long_description=long_description,
    url="https://github.com/Nova-DevTeam/nova-backtest",
    packages=find_packages(),
    install_requires=dependencies,  # Specify your dependencies here
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    setup_requires=['setuptools_scm']
)
