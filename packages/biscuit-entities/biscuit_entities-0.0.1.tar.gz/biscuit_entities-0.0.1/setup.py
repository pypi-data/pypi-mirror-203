from setuptools import setup, find_packages

VERSION = "0.0.1"
DESCRIPTION = "An library for defining structured entities in Python."
LONG_DESCRIPTION = "An entity/property library that allows consumers to define classes with mandatory traits and out-of-the-box serialization."

setup(
    name="biscuit_entities",
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author="Jacob Paisley",
    author_email="jacobpaisley97@gmail.com",
    license="MIT",
    packages=find_packages(),
    install_requires=[],
    keywords="conversion",
    classifiers= [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ]
)
