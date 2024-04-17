from setuptools import find_packages, setup

from ant import __version__

name = "ant"
version = __version__
description = "ant"
url = ""

setup(name=name,
      version=version,
      packages=find_packages(exclude=["tests"]),
      description=description,
      url=url)
