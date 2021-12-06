from setuptools import setup
import lzrw1_kh

VERSION = lzrw1_kh.__version__

setup(
    name="python-lzrw1-kh",
    description="A pure Python implementation of LZRW1/KH compression algorithm",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="http://github.com/nmantani/python-lzrw1-kh",
    license="BSD 2-clause",
    author="Nobutaka Mantani",
    author_email="nobutaka@nobutaka.org",
    packages=["lzrw1_kh"],
    version=VERSION
)
