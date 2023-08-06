from setuptools import setup, find_packages
import os

setup(
    name="ZenithCore",
    version=os.getenv("LATEST_VERSION", "0.0.0.dev1"),
    description="A package for Zenith Core Libraries",
    url="https://github.com/ZenithResearch/ZenithCore",
    author="Maaz Waraich",
    author_email="waraichmaaz@gmail.com",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "sqlalchemy",
        "psycopg2-binary"
    ],
    classifiers=[
        "Programming Language :: Python :: 3.8",
    ],
    package_data={"ZenithCore": ["schemas/*.json"]},
)
