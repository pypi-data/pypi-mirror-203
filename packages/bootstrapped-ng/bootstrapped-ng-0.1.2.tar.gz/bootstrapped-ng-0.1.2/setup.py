from pathlib import Path

from setuptools import setup


def read_version():
    with (Path(__file__).with_name("bootstrapped") / "__init__.py").open() as fd:
        for line in fd:
            if line.startswith("__version__ = "):
                return line.split()[-1].strip().strip('"')


setup(
    name="bootstrapped-ng",
    version=read_version(),
    description="Implementations of the percentile based bootstrap - forked",
    long_description=open("README.rst").read(),
    author="Spencer Beecher",
    author_email="spencebeecher@gmail.com",
    maintainer="Vadim Markovtsev",
    maintainer_email="vadim@athenian.co",
    packages=["bootstrapped"],
    install_requires=[
        "numpy>=1.11.1",
        "scipy>=0.19.1",
    ],
    extras_require={
        "power": [
            "matplotlib>=1.5.3",
            "pandas>=0.18.1",
        ],
    },
    python_requires=">=3.10.0",
    url="https://github.com/athenianco/bootstrapped",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: BSD License",
    ],
)
