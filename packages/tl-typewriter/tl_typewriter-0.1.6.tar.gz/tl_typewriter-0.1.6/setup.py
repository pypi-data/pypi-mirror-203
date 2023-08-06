from pathlib import Path
from setuptools import setup


setup(
    name="tl_typewriter",
    version='0.1.6',
    description="pagination and bubble typewriter in translating manga",
    url="https://github.com/AbangTanYiHan/tl_typewriter",
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
