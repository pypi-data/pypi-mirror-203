from pathlib import Path
from setuptools import setup

long_description = (Path(__file__).parent / "README.md").read_text('utf-8').split('# Installation')[0]

setup(
    name="tl_typewriter",
    version='0.1',
    description="pagination and bubble typewriter in translating manga",
    long_description=long_description,
    url="https://github.com/AbangTanYiHan/tl",
    author="abangtan",
    license="Apache License 2.0",
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    packages=['tl_typewriter'],
    include_package_data=True,
    install_requires=[
        "fire",
        "keyboard",
        "loguru",
    ],
    entry_points={
        "console_scripts": [
        'tl_typewriter = tl_typewriter.tl_typewriter:main'
        ]
    },
)
