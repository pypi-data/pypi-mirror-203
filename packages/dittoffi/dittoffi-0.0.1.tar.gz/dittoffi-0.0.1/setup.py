# setup.py
from setuptools import setup

if __name__ == "__main__":
    setup(
        # CFFI
        ext_package="_dittoffi",
        cffi_modules="src/_dittoffi/_ffi_build.py:ffi",
    )
