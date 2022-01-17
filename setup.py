"""
    Project Setip File
"""

from setuptools import setup, find_packages


with open("README.md", "r", encoding="UTF-8") as f:
    readme = f.read()

with open("LICENSE", "r", encoding="UTF-8") as f:
    project_license = f.read()

setup(
    name="Sensor Fusion Simulation",
    version="0.1.0",
    description="Sample package for Python-Guide.org",
    long_description=readme,
    author="Hendrik Munske",
    author_email="munsman.github@gmail.com",
    url="",
    license=project_license,
    packages=find_packages(exclude=("tests", "docs")),
)
