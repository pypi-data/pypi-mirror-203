from setuptools import setup, Extension

setup(
    name='real48',
    version='1.0',
    ext_modules=[Extension('real48', ['real48tofloat.c'])],
)